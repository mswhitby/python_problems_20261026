# High Score Streak

**10 points**

**CS concepts:** Loops, comparisons, counters, tracking program state

## Scenario

A game awards bonus points for consecutive rounds that meet a score target. A round that falls below the target resets the streak.

## Parameters

- `scores` is a list of nonnegative integer scores in chronological order. `target` is a nonnegative integer.

## Expected behavior

Return the **length of the longest consecutive streak** where every score is greater than or equal to `target`. Count consecutive qualifying rounds, not the total number of qualifying rounds. Return 0 for an empty list or if no rounds qualify.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(scores, target):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution([12, 20, 18, 7, 21, 21, 21], 18)
```

**Output**

```python
3
```

### Example 2

**Input**

```python
solution([2, 3, 4], 10)
```

**Output**

```python
0
```

Return the required value rather than printing it.
