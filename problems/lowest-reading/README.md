# Thermostat Sensor Debugger

**5 points**

**CS concepts:** loops; comparisons; initialization; debugging

## Scenario

A classroom thermostat collects temperature readings. The existing code starts its lowest value at zero, causing incorrect results when all temperatures are positive. Find and repair the logic error.

## Parameters

`readings` is a nonempty list of integers, which may be positive, negative, or zero.

## Expected behavior

Return the smallest integer in the list. Keep the provided function signature.

## Your task

Edit [`solution.py`](solution.py). Keep the function name `solution` and its parameters unchanged.

```python
def solution(readings):
    # Write your code here.
```

## Examples

```python
solution([19, 23, 21])  # 19
solution([-2, 4, 0])  # -2
```

**Debugging challenge:** the starter code has an intentional error. Find and fix it.

Return the required value rather than printing it.
