# Skills Guide: App Event Type Tally

**Optional refresher — not a completed challenge solution.** Learn the fundamental skills with a different example, then return to [App Event Type Tally](README.md).

## What you'll practice

| Skill | What it does |
|---|---|
| List | Stores a sequence of events |
| `for` loop | Visits each event once |
| Dictionary | Stores a count associated with each category |
| `.lower()` | Normalizes capitalization |
| `+= 1` | Increases a counter |
| `return` | Gives the finished dictionary back |

## 1. Lists and loops

An application can record a sequence of activities in a **list**:

```python
activities = ['Walk', 'Read', 'WALK']
for activity in activities:
    print(activity)
```

The loop runs once for each entry. `activity` holds **one string at a time**, not the whole list.

## 2. Dictionary keys and values

A **dictionary** connects keys with values. A key might be a category name; its value might be the number of times that category has occurred.

```python
totals = {
    'water': 0,
    'juice': 0,
}
totals['water'] += 1
totals['water'] += 1
print(totals)
```

**Output**

```python
{'water': 2, 'juice': 0}
```

`totals['water'] += 1` is shorthand for `totals['water'] = totals['water'] + 1`. The counts begin at zero because nothing has been counted yet.

## 3. Normalizing capitalization

Dictionary keys are case-sensitive: `'Water'` and `'water'` are different strings. Normalize the spelling **before** using it as a dictionary key.

```python
drink = 'WATER'
normalized = drink.lower()
print(normalized)  # 'water'
```

`.lower()` returns a **new string**. It doesn't change the original string automatically.

## 4. Worked example — Count drink choices

**Different task:** A school club counts water and juice requests, regardless of capitalization. The result must contain both keys, even when one drink wasn't requested.

```python
def count_drinks(orders):
    totals = {
        'water': 0,
        'juice': 0,
    }
    for drink in orders:
        category = drink.lower()
        totals[category] += 1
    return totals
```

**Input**

```python
count_drinks(['WATER', 'juice', 'Water'])
```

**Output**

```python
{'water': 2, 'juice': 1}
```

### Trace the dictionary

| Current input | Normalized key | Water count | Juice count |
|---|---|---:|---:|
| Before loop | — | 0 | 0 |
| `'WATER'` | `'water'` | 1 | 0 |
| `'juice'` | `'juice'` | 1 | 1 |
| `'Water'` | `'water'` | 2 | 1 |

This example depends on the input being limited to the known choices. The exercise in your README also tells you exactly which categories to expect.

## Understanding the provided starter code

The App Event Type Tally starter already creates a dictionary with the required categories and zero counts. You do **not** need to invent another data structure just to store those totals.

Your job is to decide how to process the input list, update the appropriate values, and give the finished result back. The dictionary's existing keys and zero values are intentional.

## Common mistakes to watch for

- **Using the input text as-is:** `'CLICK'` and `'click'` are different dictionary keys unless normalized.
- **Replacing a count instead of incrementing it:** assigning `1` every time loses earlier events.
- **Starting with missing keys:** the expected dictionary includes categories that have a count of zero.
- **Changing the dictionary but never returning it:** without an explicit `return`, Python returns `None`.
- **Returning just a number:** the challenge expects a dictionary with all category keys.
- **Assuming an empty list needs special treatment:** think about what your already initialized counters contain when no loop iterations occur.

## Check your understanding

1. What value does `{'water': 0, 'juice': 0}['juice']` produce?
2. What is `'JuIcE'.lower()`?
3. If you run `totals['water'] += 1` three times, starting from zero, what value is stored?

<details>
<summary>Reveal the practice answers</summary>

1. `0`
2. `'juice'`
3. `3`

</details>

## Hints for App Event Type Tally

Try your own approach first; open the hints only if necessary.

<details>
<summary>Hint 1 — What does the starter already do?</summary>

Notice that the dictionary is created with every required key and a starting count. What work is still missing between creating it and returning the result?

</details>

<details>
<summary>Hint 2 — How do you handle capitalization?</summary>

Before using an event name as a dictionary key, consider making its capitalization consistent.

</details>

<details>
<summary>Hint 3 — How do you count repeats?</summary>

Look at the counter example above. Each occurrence should increase the matching category's value without affecting the other categories.

</details>
