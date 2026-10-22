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
    lowest = 0
    for reading in readings:
        if reading < lowest:
            lowest = reading
    return lowest
```

## Examples

### Example 1

**Input**

```python
solution([19, 23, 21])
```

**Output**

```python
19
```

### Example 2

**Input**

```python
solution([-2, 4, 0])
```

**Output**

```python
-2
```

**Debugging challenge:** the starter code has an intentional error. Find and fix it.

Return the required value rather than printing it.
