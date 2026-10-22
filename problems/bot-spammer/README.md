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

### Example 1

**Input**

```python
solution(False, 2, 3)
```

**Output**

```python
True
```

### Example 2

**Input**

```python
solution(False, 3, 3)
```

**Output**

```python
True
```

### Example 3

**Input**

```python
solution(False, 4, 3)
```

**Output**

```python
False
```

### Example 4

**Input**

```python
solution(True, 2, 3)
```

**Output**

```python
False
```

Return the required value rather than printing it.
