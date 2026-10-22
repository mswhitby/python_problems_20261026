# 3D Object Volume Bug

**5 points**

**CS concepts:** syntax errors; debugging; arithmetic

## Scenario

A game designer needs the volume of a cube-shaped obstacle. The existing Python code has a typo that prevents it from running. Identify the syntax error and repair it.

## Parameters

`a` is an integer representing the length of a cube's edge. Edge lengths are nonnegative because physical cubes cannot have negative dimensions.

## Expected behavior

Return `a` cubed: `a * a * a`. Keep the starter function and do not print the result.

## Your task

Edit [`solution.py`](solution.py). Keep the function name `solution` and its parameters unchanged.

```python
def solution(a):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution(4)
```

**Output**

```python
4
```

### Example 2

**Input**

```python
solution(0)
```

**Output**

```python

```

**Debugging challenge:** the starter code has an intentional error. Find and fix it.

Return the required value rather than printing it.
