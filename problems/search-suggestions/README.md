# Search Suggestions

**10 points**

## Challenge

From a list of suggestion strings, return at most the first three that begin with `typed`. Matching is case-insensitive, but retain the original wording and order. An empty `typed` matches every entry. Return an empty list for no matches.

## Your task

Open [`solution.py`](solution.py). Implement the existing function without renaming `solution` or changing the specified parameters.

```python
def solution(suggestions, typed):
    # Your code goes here.
```

## Examples

```python
solution(['Python', 'pyramid', 'Java', 'pycharm'], 'py')  # ['Python', 'pyramid', 'pycharm']
solution(['Cats', 'Dogs'], 'z')  # []
```

Return the requested value rather than printing it.
