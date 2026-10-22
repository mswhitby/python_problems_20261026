# Classroom Charging Queue

**10 points**

**CS concepts:** Lists, dictionaries, filtering, inclusive comparisons

## Scenario

Before a robotics lab, the teacher checks the classroom charging cart. Some devices have enough battery to get through the lesson; others should be charged first.

## Parameters

`devices` is a list of dictionaries with two keys: `name` (a string) and `battery` (an integer percentage from 0 to 100). Device names are unique.

## Expected behavior

Return a list of names of devices with battery levels **25 or below**, keeping the original device order. A device at exactly 25% should be included. Return an empty list when none qualify.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(devices):
    # Write your code here.
```

## Examples

```python
solution([{'name': 'Tablet A', 'battery': 25}, {'name': 'Robot B', 'battery': 83}, {'name': 'Tablet C', 'battery': 4}])  # ['Tablet A', 'Tablet C']
solution([])  # []
```

Return the required value rather than printing it.
