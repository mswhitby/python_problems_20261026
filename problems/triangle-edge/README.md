# Triangle Frame Safety Check

**5 points**

**CS concepts:** triangle inequality; upper bounds

## Scenario

A robotics team is building a triangular brace with two fixed bars. They need to know the longest integer length the third bar could have while still forming a triangle.

## Parameters

`side1` and `side2` are positive integers measured in centimeters.

## Expected behavior

Return the largest possible positive integer length for the third side. No side can equal or exceed the sum of the other two.

## Your task

Edit [`solution.py`](solution.py). Keep the function name `solution` and its parameters unchanged.

```python
def solution(side1, side2):
    # Write your code here.
```

## Examples

```python
solution(6, 11)  # 16
solution(3, 3)  # 5
```

Return the required value rather than printing it.
