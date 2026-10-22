"""Unprivileged changed-file test runner. No credentials or write tokens."""
import base64
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import zlib

HERE = Path(__file__).resolve().parent
MANIFEST = json.loads((HERE / "manifest.json").read_text())["challenges"]
RAW = zlib.decompress(base64.urlsafe_b64decode((HERE / "cases.b64").read_text().strip()))
TESTS = json.loads(RAW)
if set(MANIFEST) != set(TESTS) or not all(TESTS.values()):
    raise SystemExit("Test case manifest is inconsistent")

def run():
    student = Path(sys.argv[1]).resolve()
    changed = subprocess.check_output(["git","-C",str(student),"diff","--name-only","HEAD^1","HEAD"],text=True).splitlines()
    pattern = re.compile(r"^problems/([a-z0-9-]+)/solution\.py$")
    slugs = sorted({m.group(1) for file in changed if (m := pattern.match(file)) and m.group(1) in MANIFEST})
    if not slugs:
        print("No recognized challenge solutions changed")
        return
    Path("grading-feedback").mkdir(exist_ok=True)
    scores = {}
    lines = ["## Python challenge results","","| Challenge | Tests passed | Points |","|---|---:|---:|"]
    feedback = []
    for slug in slugs:
        cases = TESTS[slug]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "results.json"
            case_file = Path(directory) / "cases.json"
            case_file.write_text(json.dumps(cases))
            cmd = [sys.executable,str(HERE / "worker.py"),str(student),slug,str(case_file),str(output)]
            try:
                completed = subprocess.run(cmd, timeout=12, capture_output=True, text=True)
                if completed.returncode != 0 or not output.exists():
                    results = [{"name":c[0],"pass":False,"message":"Program failed or exceeded resource limit"} for c in cases]
                else:
                    results = json.loads(output.read_text())
                    if len(results) != len(cases):
                        raise ValueError("Incomplete test results")
            except (subprocess.TimeoutExpired, ValueError):
                results = [{"name":c[0],"pass":False,"message":"Program timed out or returned invalid test results"} for c in cases]
        passed = sum(case.get("pass") is True for case in results)
        points = round(MANIFEST[slug]*passed/len(cases),2)
        scores[slug] = points
        lines.append(f"| {slug} | {passed}/{len(cases)} | {points:.2f}/{MANIFEST[slug]} |")
        feedback.extend(["",f"### {slug}",""])
        for case in results:
            outcome = "Passed" if case.get("pass") else "Failed"
            message = case.get("message","")
            feedback.append(f"- **{case.get('name','Case')}**: {outcome}"+(f" — {message}" if message else ""))
    lines.extend(["",f"**Current submission: {sum(scores.values()):.2f}/{sum(MANIFEST[s] for s in slugs)} points**","",*feedback])
    text = "\n".join(lines)
    (Path("grading-feedback")/"details.md").write_text(text[:48000])
    result = {"version":2,"pr_number":int(os.environ["GRADE_PR_NUMBER"]),
        "head_sha":os.environ["GRADE_HEAD_SHA"],"run_id":int(os.environ["GITHUB_RUN_ID"]),
        "run_attempt":int(os.environ.get("GITHUB_RUN_ATTEMPT","1")),"scores":scores}
    (Path("grading-feedback")/"grade.json").write_text(json.dumps(result))
    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary,"a") as f:
            f.write(text[:48000])
    print(text[:20000])

if __name__ == "__main__":
    run()
