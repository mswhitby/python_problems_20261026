# Bot Spammer

**5 points**

**CS concepts:** boolean logic; conditions; rate limiting; parameters

## Scenario

You are creating a bot that posts comments to a social-media thread. Too many requests can overload the site or get an account muted. Your code implements **rate limiting**, a rule that restricts how often software may attempt an action.

## Parameters

- `passed` (**boolean**): whether the **previous** attempt succeeded.
- `attempt` (**positive integer**): the number of the attempt about to be made, beginning at 1.
- `limit` (**nonnegative integer**): the highest permitted attempt number.

## Expected behavior

Return `True` only when the previous attempt **did not pass** AND the **current attempt is not over the limit**. The final permitted attempt is allowed; return `False` otherwise.

## Your task

Edit [`solution.py`](solution.py). Keep the function name `solution` and its parameters unchanged.

```python
def solution(passed, attempt, limit):
    # Write your code here.
```

## Examples

```python
solution(False, 2, 3)  # True
solution(False, 3, 3)  # True
solution(False, 4, 3)  # False
solution(True, 2, 3)  # False
```

Return the required value rather than printing it.
