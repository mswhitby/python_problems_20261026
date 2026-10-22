# Upload Space Gatekeeper

**5 points**

**CS concepts:** comparison operators; arithmetic; boundary values

## Scenario

A student is saving a project backup to a storage drive. Before transferring the file, the application checks available space to avoid a failed upload.

## Parameters

`capacity`, `used`, and `size` are nonnegative integers measured in megabytes. `used` never exceeds `capacity`.

## Expected behavior

Return `True` if the file fits without exceeding the drive's capacity, or `False` otherwise. Filling the last available megabyte is allowed.

## Your task

Edit [`solution.py`](solution.py). Keep the function name `solution` and its parameters unchanged.

```python
def solution(capacity, used, size):
    # Write your code here.
```

## Examples

```python
solution(256, 240, 16)  # True
solution(256, 240, 20)  # False
```

Return the required value rather than printing it.
