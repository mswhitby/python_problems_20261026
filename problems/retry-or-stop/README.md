# Retry or Stop?

**5 points**

## Challenge

Return `True` only when a previous request failed AND the number of attempts already made is below the maximum limit. `failed` is a boolean; the other inputs are nonnegative integers.

## Your task

Open [`solution.py`](solution.py). Implement the existing function without renaming `solution` or changing the specified parameters.

```python
def solution(failed, attempts, limit):
    # Your code goes here.
```

## Examples

```python
solution(True, 2, 3)  # True
solution(True, 3, 3)  # False
solution(False, 2, 3)  # False
```

Return the requested value rather than printing it.
