# Ticket Queue Counter

**5 points**

**CS concepts:** parameters; integer arithmetic

## Scenario

An event kiosk assigns numbered tickets to visitors. After processing one ticket, the screen must display the number of the next ticket in line.

## Parameters

- `num` is an integer. Tests may use negative numbers or zero.

## Expected behavior

Return the integer that comes immediately after `num`.

## Your task

Edit [`solution.py`](solution.py). Keep the function name `solution` and its parameters unchanged.

```python
def solution(num):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution(49)
```

**Output**

```python
50
```

### Example 2

**Input**

```python
solution(-1)
```

**Output**

```python
0
```

Return the required value rather than printing it.
