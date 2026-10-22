# Co-op Lobby Notification

**5 points**

**CS concepts:** string formatting; exact output

## Scenario

A multiplayer game displays a notification when another player joins. The username should appear exactly as entered so friends can recognize one another.

## Parameters

- `username` is a nonempty string containing letters, digits, hyphens, or underscores.

## Expected behavior

Return the exact text `Player NAME entered the lobby.` with NAME replaced by the supplied username. Include the final period.

## Your task

Edit [`solution.py`](solution.py). Keep the function name `solution` and its parameters unchanged.

```python
def solution(username):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution('fox-9')
```

**Output**

```python
'Player fox-9 entered the lobby.'
```

### Example 2

**Input**

```python
solution('NeoCoder')
```

**Output**

```python
'Player NeoCoder entered the lobby.'
```

Return the required value rather than printing it.
