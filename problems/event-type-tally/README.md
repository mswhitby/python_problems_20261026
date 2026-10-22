# App Event Type Tally

**10 points**

**CS concepts:** Dictionaries, counters, string normalization

## Scenario

Developers record simple app interactions to learn how people navigate their software. Different devices sometimes capitalize the same event differently, but each event should contribute to the correct count.

## Parameters

`events` is a list of strings. Every entry is a capitalization variant of `click`, `view`, or `submit`.

## Expected behavior

Return a dictionary with **exactly** the keys `click`, `view`, and `submit`. Count the occurrences of each event without regard to case. Include an event key with a count of 0 if it never occurs.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(events):
    # Write your code here.
```

## Examples

```python
solution(['CLICK', 'view', 'Click', 'submit'])  # {'click': 2, 'view': 1, 'submit': 1}
solution([])  # {'click': 0, 'view': 0, 'submit': 0}
```

Return the required value rather than printing it.
