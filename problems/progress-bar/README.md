# Draw a Progress Bar

**10 points**

## Challenge

Given an integer percentage from 0 to 100 in increments of 10, return a 10-character text bar inside square brackets. Use `#` for each completed 10% and `-` for each unfinished 10%, then a space and the percent value followed by `%`.

## Your task

Open [`solution.py`](solution.py). Implement the existing function without renaming `solution` or changing the specified parameters.

```python
def solution(percent):
    # Your code goes here.
```

## Examples

```python
solution(0)  # '[----------] 0%'
solution(50)  # '[#####-----] 50%'
solution(100)  # '[##########] 100%'
```

Return the requested value rather than printing it.
