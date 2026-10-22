# Which Devices Need Charging?

**10 points**

## Challenge

Each element of `devices` is a dictionary with a string `name` and an integer `battery` percentage from 0 to 100. Return a list of names whose battery values are strictly below 20. Preserve input order; if none qualify, return an empty list.

## Your task

Open [`solution.py`](solution.py). Implement the existing function without renaming `solution` or changing the specified parameters.

```python
def solution(devices):
    # Your code goes here.
```

## Examples

```python
solution([{'name': 'Phone', 'battery': 12}, {'name': 'Tablet', 'battery': 20}])  # ['Phone']
solution([])  # []
```

Return the requested value rather than printing it.
