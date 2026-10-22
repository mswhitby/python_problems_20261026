# Classroom Topic Tag

**5 points**

**CS concepts:** strings; whitespace; normalization

## Scenario

A class discussion platform turns topics into searchable hashtags. Students might enter extra spaces and capital letters, so the app must standardize the text before posting.

## Parameters

`word` contains at least one letter, possibly multiple words and extra whitespace. It contains no punctuation.

## Expected behavior

Remove extra whitespace, make all letters lowercase, join words with underscores, and prefix the result with exactly one `#`.

## Your task

Edit [`solution.py`](solution.py). Keep the function name `solution` and its parameters unchanged.

```python
def solution(word):
    # Write your code here.
```

## Examples

```python
solution('  Game   Design  ')  # '#game_design'
solution('Robotics')  # '#robotics'
```

Return the required value rather than printing it.
