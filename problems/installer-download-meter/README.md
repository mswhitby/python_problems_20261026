# Installer Download Meter

**10 points**

**CS concepts:** String repetition, arithmetic, exact output

## Scenario

A software installer shows its progress in a text-only terminal. The meter has ten sections, so each filled section represents another 10% completed.

## Parameters

- `percent` is an integer from 0 to 100, inclusive, always in increments of 10.

## Expected behavior

Create a ten-character meter with `#` for each finished section and `.` for each remaining section. Surround the meter with `|` characters. Add a single space, the percentage, and `%`. Return the entire string.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(percent):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution(30)
```

**Output**

```python
'|###.......| 30%'
```

### Example 2

**Input**

```python
solution(0)
```

**Output**

```python
'|..........| 0%'
```

### Example 3

**Input**

```python
solution(100)
```

**Output**

```python
'|##########| 100%'
```

Return the required value rather than printing it.
