# Mood-to-Music Label

**5 points**

**CS concepts:** string methods; normalization; return values

## Scenario

A music app automatically names listening sessions. People sometimes type moods with extra spaces or inconsistent capitalization. Clean the input so every session title looks consistent.

## Parameters

`mood` is a string containing at least one letter after whitespace is removed. It may contain multiple words.

## Expected behavior

Remove outer whitespace, capitalize the first letter of every word, and append ` Session`. Return the resulting string.

## Your task

Edit [`solution.py`](solution.py). Keep the function name `solution` and its parameters unchanged.

```python
def solution(mood):
    # Write your code here.
```

## Examples

```python
solution('  rainy day  ')  # 'Rainy Day Session'
solution('CODING')  # 'Coding Session'
```

Return the required value rather than printing it.
