# Lab Procedure Formatter

**10 points**

**CS concepts:** Lists, counters, string formatting

## Scenario

A digital lab guide stores safety instructions as plain text. To make the guide easier to follow, the app adds a numbered label to each instruction before showing it on a screen.

## Parameters

- `steps` is a list of strings in the order they should be completed.

## Expected behavior

Return a **new list** of strings. Prefix each instruction with `Step N: ` where N begins at 1 and increases by one. Preserve the original instruction text and order. Return an empty list for an empty input.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(steps):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution(['Charge drone', 'Connect controller'])
```

**Output**

```python
['Step 1: Charge drone', 'Step 2: Connect controller']
```

### Example 2

**Input**

```python
solution([])
```

**Output**

```python
[]
```

Return the required value rather than printing it.
