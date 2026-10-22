"""Trusted cumulative feedback and leaderboard publisher.

Runs only from main after the read-only PR workflow. Never executes student code.
"""
import base64
from datetime import datetime
import json
import math
import os
from pathlib import Path
import re
import urllib.request
from zoneinfo import ZoneInfo

MANIFEST=json.loads((Path(__file__).resolve().parents[1]/"grading/manifest.json").read_text())["challenges"]
BOT="github-actions[bot]"
MARKER="<!-- python-challenge-grade:v2 "
PATTERN=re.compile(r"<!-- python-challenge-grade:v2 ([A-Za-z0-9_+/=.-]+) -->")
MAX_PAGES=25

def api(method,endpoint,payload=None):
    raw=None if payload is None else json.dumps(payload).encode("utf-8")
    headers={"Authorization":"Bearer "+os.environ["GITHUB_TOKEN"],
      "Accept":"application/vnd.github+json",
      "X-GitHub-Api-Version":"2022-11-28",
      "User-Agent":"classroom-python-grading"}
    if raw is not None:headers["Content-Type"]="application/json"
    url="https://api.github.com/repos/"+os.environ["GITHUB_REPOSITORY"]+endpoint
    request=urllib.request.Request(url,data=raw,method=method,headers=headers)
    with urllib.request.urlopen(request,timeout=25) as response:
        return json.load(response) if response.status!=204 else None

def all_pages(endpoint):
    result=[]
    for page in range(1,MAX_PAGES+1):
        suffix="&" if "?" in endpoint else "?"
        batch=api("GET",endpoint+f"{suffix}per_page=100&page={page}")
        result.extend(batch)
        if len(batch)<100:return result
    raise RuntimeError("More than 2500 GitHub records; grade history not complete")

def clean_scores(values):
    if not isinstance(values,dict) or not 1<=len(values)<=len(MANIFEST):
        raise ValueError("Invalid score map")
    clean={}
    for name,score in values.items():
        if name not in MANIFEST or isinstance(score,bool) or not isinstance(score,(int,float)):
            raise ValueError("Invalid score entry")
        if not math.isfinite(score) or not 0<=score<=MANIFEST[name]:
            raise ValueError("Score exceeds assigned challenge points")
        clean[name]=round(float(score),2)
    return clean

def unpack_comment(body,author):
    found=PATTERN.findall(body or "")
    if not found:return None
    try:
        record=json.loads(base64.urlsafe_b64decode(found[-1]))
        if record.get("version")!=2 or record.get("author")!=author:return None
        if not isinstance(record.get("run_id"),int) or record["run_id"]<1:return None
        if not isinstance(record.get("run_attempt"),int) or record["run_attempt"]<1:return None
        if not re.fullmatch("[a-f0-9]{40}",record.get("head_sha","")):return None
        record["scores"]=clean_scores(record["scores"])
        return record
    except (ValueError,KeyError,TypeError):return None

def encode(record):
    raw=json.dumps(record,sort_keys=True,separators=(",",":")).encode("utf-8")
    return MARKER+base64.urlsafe_b64encode(raw).decode("ascii")+" -->"

def read_history():
    prs={item["number"]:item for item in all_pages("/pulls?state=all")}
    latest={}
    for comment in all_pages("/issues/comments"):
        if comment.get("user",{}).get("login")!=BOT:continue
        try:number=int(comment["issue_url"].split("/")[-1])
        except (KeyError,TypeError,ValueError):continue
        pr=prs.get(number)
        if not pr:continue
        author=pr["user"]["login"]
        record=unpack_comment(comment.get("body"),author)
        if not record:continue
        order=(record["run_id"],record["run_attempt"])
        if number not in latest or order>latest[number][0]:
            latest[number]=(order,author,record,comment["id"])
    return prs,latest

def scores_by_author(prs,history):
    users={}
    for number,(order,author,record,_id) in history.items():
        if prs[number].get("title","").strip().upper().startswith("DO NOT MERGE"):
            continue
        scores=users.setdefault(author,{})
        for slug,value in record["scores"].items():
            if slug not in scores or order>scores[slug][0]:
                scores[slug]=(order,value)
    return users

def comment_body(scores,history,details,record):
    current_total=sum(scores.values())
    possible=sum(MANIFEST[slug] for slug in scores)
    all_scores={slug:item[1] for slug,item in history.items()}
    earned=sum(all_scores.values())
    solved=sum(value>=MANIFEST[slug]-0.005 for slug,value in all_scores.items())
    lines=[
      "## Python challenge progress","",
      f"**This submission: {current_total:.2f}/{possible} points**",
      f"**Overall competition points: {earned:.2f}**",
      f"**Solved: {solved} · Attempted: {len(all_scores)}**","",
      "| Challenge | Status | Points |","|---|---|---:|"]
    for slug,maximum in MANIFEST.items():
        if slug in scores:status="Graded in this PR"
        elif slug in all_scores:status="Graded previously"
        else:continue
        lines.append(f"| {slug} | {status} | {all_scores.get(slug,0):.2f}/{maximum} |")
    lines.extend(["","<details><summary>Show test feedback</summary>","",details[:28000],"","</details>","",
       "Challenge points are not official classroom grades.","",encode(record)])
    result="\n".join(lines)
    if len(result)>60000:raise ValueError("Feedback exceeds GitHub comment limit")
    return result

def render_leaderboard(original,users):
    lines=original.splitlines(keepends=True)
    title="| Rank | GitHub username | Solved | Attempted | Points |"
    start=next((i for i,line in enumerate(lines) if line.strip()==title),None)
    if start is None:raise ValueError("Leaderboard heading missing; refusing to replace custom content")
    end=start+1
    while end<len(lines) and lines[end].lstrip().startswith("|"):end+=1
    ranking=[]
    for user,graded in users.items():
        points={slug:item[1] for slug,item in graded.items()}
        total=round(sum(points.values()),2)
        solved=sum(value>=MANIFEST[slug]-0.005 for slug,value in points.items())
        ranking.append((user,total,solved,len(points)))
    ranking.sort(key=lambda x:(-x[1],-x[2],x[0].lower()))
    table=[title,"|---:|---|---:|---:|---:|"]
    previous=None
    position=0
    for row_number,(name,points,solved,attempted) in enumerate(ranking,1):
        if points!=previous:position=row_number;previous=points
        table.append(f"| {position} | `{name}` | {solved} | {attempted} | {points:.2f} |")
    output="".join(lines[:start])+"\n".join(table)+"\n"+"".join(lines[end:])
    stamp=datetime.now(ZoneInfo("America/Chicago")).strftime("%B %d, %Y at %H:%M CT")
    return re.sub(r"(?m)^\*Last updated:[^\n]*\*$",f"*Last updated: {stamp}*",output,count=1)

def save_leaderboard(users):
    current=api("GET","/contents/LEADERBOARD.md?ref=main")
    before=base64.b64decode(current["content"]).decode("utf-8")
    after=render_leaderboard(before,users)
    if after==before:return
    api("PUT","/contents/LEADERBOARD.md",{
      "branch":"main","sha":current["sha"],"message":"Update challenge leaderboard",
      "content":base64.b64encode(after.encode("utf-8")).decode("ascii")})
    print("Leaderboard updated")

def main():
    workflow=json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())["workflow_run"]
    if workflow.get("event")!="pull_request" or workflow.get("name")!="Grade Python Pull Request":
        raise SystemExit("Unexpected grader event")
    data=Path("grade-download/grade.json")
    details=Path("grade-download/details.md")
    if not data.exists() or not details.exists():
        raise SystemExit("No completed challenge grading artifact")
    if data.stat().st_size>12000 or details.stat().st_size>50000:
        raise SystemExit("Unexpected grading artifact size")
    submitted=json.loads(data.read_text())
    if submitted.get("version")!=2:raise SystemExit("Unexpected grader version")
    number=submitted.get("pr_number")
    sha=submitted.get("head_sha")
    if not isinstance(number,int) or number<1 or not isinstance(sha,str) or not re.fullmatch("[a-f0-9]{40}",sha):
        raise SystemExit("Invalid PR or commit")
    if submitted.get("run_id")!=workflow["id"] or submitted.get("run_attempt")!=workflow.get("run_attempt",1):
        raise SystemExit("Stale or mismatched grading run")
    scores=clean_scores(submitted.get("scores"))
    pr=api("GET",f"/pulls/{number}")
    if (pr.get("head",{}).get("sha")!=sha or workflow.get("head_sha")!=sha or
        pr.get("base",{}).get("ref")!="main" or
        pr.get("head",{}).get("repo",{}).get("full_name")!=workflow.get("head_repository",{}).get("full_name")):
        raise SystemExit("Grader run doesn't match current PR head")
    author=pr["user"]["login"]
    prs,previous=read_history()
    current=previous.get(number)
    order=(workflow["id"],workflow.get("run_attempt",1))
    if current and current[0]>order:
        raise SystemExit("A newer grading result already exists")
    record={"version":2,"author":author,"run_id":order[0],"run_attempt":order[1],"head_sha":sha,"scores":scores}
    previous[number]=(order,author,record,current[3] if current else None)
    users=scores_by_author(prs,previous)
    body=comment_body(scores,users.get(author,{}),details.read_text(),record)
    if current and current[3]:api("PATCH",f"/issues/comments/{current[3]}",{"body":body})
    else:api("POST",f"/issues/{number}/comments",{"body":body})
    print("Posted cumulative feedback for PR",number)
    save_leaderboard(users)

if __name__=="__main__":
    main()
