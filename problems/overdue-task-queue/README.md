# Assignment Deadline Queue

**10 points**

**CS concepts:** Compound boolean conditions, dictionaries, filtering

## Scenario

A class project board reminds students which unfinished tasks require attention. Some tasks are overdue, while others were completed or are not yet due.

## Parameters

- `tasks`: a list of dictionaries describing the assignments.
  - `title`: a string naming the assignment.
  - `due`: an integer day number for the deadline.
  - `complete`: a boolean indicating whether it is finished.
- `today`: an integer day number on the same scale as `due`.

## Expected behavior

Return a list of titles for tasks with `complete=False` and `due` **strictly earlier** than `today`. Keep their original order. A task due today isn't overdue. Return an empty list if none qualify.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(tasks, today):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution(
    [
        {'title': 'Storyboard', 'due': 10, 'complete': False},
        {'title': 'Sprites', 'due': 11, 'complete': False},
        {'title': 'Menu', 'due': 8, 'complete': True}
    ],
    11
)
```

**Output**

```python
'Storyboard']
```

### Example 2

**Input**

```python
solution([], 12)
```

**Output**

```python
]
```

Return the required value rather than printing it.
