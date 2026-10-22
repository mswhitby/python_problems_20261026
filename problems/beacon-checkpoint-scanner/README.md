# Beacon Checkpoint Scanner

**25 points**

**CS concepts:** Loops, modular arithmetic, number patterns, accumulated results

## Scenario

In a research simulation, checkpoints have positive integer IDs. A checkpoint `n` is synchronized when `(2 ** n + 1)` is evenly divisible by `(2 * n + 1)`. This mathematical property is called the Curzon condition. You have been given the task of identifying all integers in a specified range that meet the Curzon condition.

## Parameters

- `start`: the first positive integer checkpoint ID to examine.
- `end`: the last positive integer checkpoint ID to examine.

Both endpoints are included, and `1 <= start <= end <= 200`.

## Expected behavior

Return an ascending **list of all checkpoint IDs** from `start` to `end` that meet the condition. A checkpoint qualifies when the division remainder is zero. Return an empty list if none qualify.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(start, end):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution(1, 6)
```

**Output**

```python
[1, 2, 5, 6]
```

### Example 2

**Input**

```python
solution(7, 10)
```

**Output**

```python
[9]
```

### Example 3

**Input**

```python
solution(3, 4)
```

**Output**

```python
[]
```

Return the required value rather than printing it.
