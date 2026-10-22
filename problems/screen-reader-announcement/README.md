# Screen Reader Announcement Composer

**25 points**

**CS concepts:** String normalization, deduplication, preserving order, edge cases

## Scenario

An accessibility app reads selected items aloud. Imported labels may contain leading spaces, empty entries, or the same label repeated with different capitalization. Prepare a clean announcement that sounds natural.

## Parameters

- `labels`: a list of strings, possibly empty or containing surrounding whitespace.
- `separator`: a nonempty single word such as `and` or `or`.

## Expected behavior

Process labels in their original order. Strip spaces at both ends of each label, discard empty labels, and remove duplicates **ignoring case**, keeping the first spelling and its place in the list. If no labels remain, return `''`; with one, return that label; with two, join them with a space, the separator, and another space. With three or more, join earlier labels using `, ` and place `, separator ` before the last (Oxford comma).

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(labels, separator):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution(['  Alpha  ', '', 'beta', 'ALPHA', 'Gamma'], 'and')
```

**Output**

```python
'Alpha, beta, and Gamma'
```

### Example 2

**Input**

```python
solution(['oak', 'pine'], 'or')
```

**Output**

```python
'oak or pine'
```

### Example 3

**Input**

```python
solution(['  '], 'and')
```

**Output**

```python
''
```

Return the required value rather than printing it.
