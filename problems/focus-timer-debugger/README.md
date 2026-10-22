# Focus Timer Debugger

**10 points**

**CS concepts:** Dictionaries, loops, optional parameters, debugging

## Scenario

A study timer records time spent on different assignments. Its current code adds every task's minutes even when a student wants to see only active work. Repair the logic so the optional setting has the intended effect.

## Parameters

- `tasks`: a list of dictionaries containing `minutes` (a nonnegative integer) and `paused` (a boolean).
- `include_paused`: an optional boolean parameter. Its default value is `True`.

## Expected behavior

If `include_paused` is `True`, include every task. If it is `False`, skip tasks marked `paused=True`. Return the total number of minutes as an integer. An empty task list returns 0.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(tasks, include_paused=True):
    total = 0
    for task in tasks:
        total += task["minutes"]
    return total
```

## Examples

### Example 1

**Input**

```python
solution([{'minutes': 14, 'paused': False}, {'minutes': 7, 'paused': True}], False)
```

**Output**

```python
14
```

### Example 2

**Input**

```python
solution([{'minutes': 14, 'paused': False}, {'minutes': 7, 'paused': True}])
```

**Output**

```python
21
```

### Example 3

**Input**

```python
solution([], False)
```

**Output**

```python
0
```

**Debugging challenge:** the starter code has an intentional mistake. Find and repair it.

Return the required value rather than printing it.
