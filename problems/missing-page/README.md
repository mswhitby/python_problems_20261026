# Missing Library Badge

**10 points**

**CS concepts:** Lists, number sequences, problem decomposition

## Scenario

A school gives visitors badges numbered consecutively from 1. During inventory, a librarian has a shuffled list of the returned badges and discovers that exactly one badge is missing.

## Parameters

`total` is a positive integer for the final badge number. `badges` contains each number from 1 through `total` exactly once except for one missing number. The numbers may appear in any order.

## Expected behavior

Return the missing badge number as an integer. For a single-badge collection, the list is empty, and the missing number is 1.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(badges, total):
    # Write your code here.
```

## Examples

```python
solution([4, 2, 1, 6, 3], 6)  # 5
solution([3, 2], 3)  # 1
solution([], 1)  # 1
```

Return the required value rather than printing it.
