# Feature Switch Inverter

**10 points**

**CS concepts:** Boolean values, logical negation, return types

## Scenario

An app developer is testing the on/off switch for an accessibility setting. When the user presses the switch, the setting should move to the opposite state.

## Parameters

- `arg` is always a boolean: `True` (enabled) or `False` (disabled).

## Expected behavior

Return the opposite boolean value. The output must be `True` or `False`, not text or an integer.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(arg):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution(False)
```

**Output**

```python
True
```

### Example 2

**Input**

```python
solution(True)
```

**Output**

```python
False
```

Return the required value rather than printing it.
