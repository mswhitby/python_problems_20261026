# Classroom Topic Tag

**10 points**

**CS concepts:** strings; whitespace; normalization

## Scenario

A class discussion platform turns topics into searchable hashtags. Students might enter extra spaces and capital letters, so the app must standardize the text before posting.

## Parameters

`word` contains at least one letter, possibly multiple words and extra whitespace. It contains no punctuation.

## Expected behavior

Remove extra whitespace. Capitalize the first letter of each word and make all remaining letters lowercase. Join the words without spaces, and prefix the result with `#` to create a **PascalCase hashtag**.

## Your task

Edit [`solution.py`](solution.py). Keep the function name `solution` and its parameters unchanged.

```python
def solution(word):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution('  Game   Design  ')
```

**Output**

```python
'#GameDesign'
```

### Example 2

**Input**

```python
solution('Robotics')
```

**Output**

```python
'#Robotics'
```

Return the required value rather than printing it.
