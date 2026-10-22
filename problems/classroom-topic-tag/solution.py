def solution(word):
    return "#" + "".join(part.capitalize() for part in word.split())
