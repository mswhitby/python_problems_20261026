# Will the Next File Fit?

**5 points**

## Challenge

A storage drive has `capacity` megabytes, with `used` already occupied. Return `True` if a new file of `size` megabytes fits, including when it fills the remaining space exactly. Inputs are nonnegative whole numbers with `used <= capacity`.

## Your task

Open [`solution.py`](solution.py). Implement the existing function without renaming `solution` or changing the specified parameters.

```python
def solution(capacity, used, size):
    # Your code goes here.
```

## Examples

```python
solution(100, 70, 30)  # True
solution(100, 70, 31)  # False
```

Return the requested value rather than printing it.
