# Join with a Final Separator

**25 points**

## Challenge

Create a human-readable phrase from a list of labels. Separate earlier items with `, `, and place the joining word `separator` before the last. With two labels, use only the joining word. Return a single label unchanged, or an empty string if there are no labels.

## Your task

Open [`solution.py`](solution.py). Implement the existing function without renaming `solution` or changing the specified parameters.

```python
def solution(labels, separator):
    # Your code goes here.
```

## Examples

```python
solution(['red', 'blue', 'green'], 'and')  # 'red, blue and green'
solution(['tea', 'coffee'], 'or')  # 'tea or coffee'
solution([], 'and')  # ''
```

Return the requested value rather than printing it.
