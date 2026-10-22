# Leave Paused Tasks Out of the Total

**10 points**

## Challenge

Fix the starter code for a task timer. `tasks` is a list of dictionaries containing `minutes` (nonnegative integer) and `paused` (boolean). Include all minutes when `include_paused` is `True`, the default; exclude paused tasks when it is `False`. An empty list produces 0.

## Your task

Open [`solution.py`](solution.py). Implement the existing function without renaming `solution` or changing the specified parameters.

```python
def solution(tasks, include_paused=True):
    # Your code goes here.
```

## Examples

```python
solution([{'minutes': 12, 'paused': False}, {'minutes': 8, 'paused': True}], False)  # 12
solution([{'minutes': 12, 'paused': False}, {'minutes': 8, 'paused': True}])  # 20
```

**Debugging challenge:** the starter code contains an error. Fix it while keeping the function signature.

Return the requested value rather than printing it.
