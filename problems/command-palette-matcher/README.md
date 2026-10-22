# Command Palette Matcher

**10 points**

**CS concepts:** Prefix matching, sorting, slicing, case-insensitive comparisons

## Scenario

A programming editor offers a command palette to help users find actions such as opening a file or running tests. Commands matching the letters typed should appear in predictable alphabetical order.

## Parameters

- `suggestions`: a list of command strings.
- `typed`: a string, which may be empty.
A command matches if its text begins with `typed`, ignoring uppercase and lowercase differences.

## Expected behavior

Find all matches, sort them alphabetically ignoring case, and return the first **four**. Preserve each matching command's original spelling and capitalization. When two entries are equal ignoring case, preserve their original order. An empty search matches all commands. Return an empty list if there are no matches.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(suggestions, typed):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution(['Open Settings', 'Run Tests', 'open Folder', 'Open File'], 'op')
```

**Output**

```python
['Open File', 'open Folder', 'Open Settings']
```

### Example 2

**Input**

```python
solution(['Run', 'Reset'], 'save')
```

**Output**

```python
[]
```

Return the required value rather than printing it.
