# Bot Spammer

**5 points**

## Challenge

You are creating a bot that automatically posts comments to a social media thread. You want to make sure that your program does not overload the system, which would result in you getting muted or banned. Write a program that limits how many times your bot attempts a post. Your program will accept three paramaters:

- `passed`: a boolean value indicating if the prior attempt passed
- `attempt`: a positive integer value indicating the number of this attempt
- `limit`: a nonnegative integer value indicating the maximum number of attempts

Return `True` only when a previous request has not passed AND the number of this attempt is not above the maximum limit.

## Your task

Open [`solution.py`](solution.py). Implement the existing function without renaming `solution` or changing the specified parameters.

```python
def solution(passed, attempt, limit):
    # Your code goes here.
```

## Examples

```python
solution(True, 2, 3)  # False
solution(True, 3, 3)  # False
solution(False, 2, 3)  # True
```

Return the requested value rather than printing it.
