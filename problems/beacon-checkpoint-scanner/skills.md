# Skills Guide: Beacon Checkpoint Scanner

**Optional refresher — not the solution to the challenge.** This guide uses a different number-selection task to show the building blocks. Read only the sections you need, then return to [the challenge](README.md).

## What you'll practice

| Skill | Why it matters |
|---|---|
| `for` loop | Repeat a check for several numbers |
| `range()` | Generate the numbers between two boundaries |
| Arithmetic operators | Calculate expressions with a changing number |
| Modulo (`%`) | Test whether division leaves a remainder |
| List and `.append()` | Collect results that pass a test |
| `return` | Give a completed list back to the caller |

## 1. Repeating a task with a loop

A loop runs the same indented block once for every value in a sequence. The variable `number` changes each time.

```python
for number in range(3, 7):
    print(number)
```

**Output**

```text
3
4
5
6
```

`range(3, 7)` includes **3** but not **7**. To include a last value stored in `last`, you can use `range(first, last + 1)`. This is called an **inclusive range**.

## 2. Arithmetic and divisibility

| Operator | Meaning | Example |
|---|---|---|
| `+` | Add | `4 + 3` is `7` |
| `**` | Raise to a power | `2 ** 3` is `8` |
| `%` | Remainder after division | `14 % 4` is `2` |
| `==` | Compare for equality | `14 % 2 == 0` is `True` |

Use `==` to **compare** values; `=` is for assigning a value to a variable.

```python
print(12 % 4)       # 0: divisible by 4
print(13 % 4)       # 1: not divisible by 4
print(12 % 4 == 0)  # True
```

Try the calculations by hand: if you can divide a number by another number with no remainder, the first number is **divisible** by the second.

## 3. Keeping qualifying results in a list

Start with an empty list. `.append()` adds one item at the end.

```python
locker_numbers = []
locker_numbers.append(4)
locker_numbers.append(8)
print(locker_numbers)
```

**Output**

```python
[4, 8]
```

Notice that `locker_numbers` is a **list**, not the string `"4, 8"`. The type of the value you return matters.

## 4. Worked example — Find numbered lockers

**Different task:** A hallway has lockers numbered from `first` to `last`. Return all locker numbers that are multiples of **4**. This uses the same Python fundamentals, but it does not test the Curzon condition.

```python
def lockers_to_check(first, last):
    selected = []
    for locker in range(first, last + 1):
        if locker % 4 == 0:
            selected.append(locker)
    return selected
```

**Input**

```python
lockers_to_check(2, 10)
```

**Output**

```python
[4, 8]
```

### Walk through the loop

| Current locker | `locker % 4` | Add to list? | List afterward |
|---:|---:|---|---|
| 2 | 2 | No | `[]` |
| 3 | 3 | No | `[]` |
| 4 | 0 | Yes | `[4]` |
| 5–7 | Not zero | No | `[4]` |
| 8 | 0 | Yes | `[4, 8]` |
| 9–10 | Not zero | No | `[4, 8]` |

The important pattern is **examine → evaluate → keep or skip**. Your challenge uses a different mathematical condition, so you'll need to work out the check yourself.

## Common mistakes to watch for

- **Leaving out the last number:** `range(first, last)` stops just before `last`.
- **Using `/` instead of `%`:** `/` computes a quotient; `%` gives the remainder.
- **Using `=` inside an `if` condition:** use `==` when asking whether two values are equal.
- **Creating the list inside the loop:** that would erase previously collected values each time.
- **Printing instead of returning:** `print(results)` displays a value, but the grader needs `return results`.
- **Returning one number instead of a list:** even one match belongs inside a list, such as `[8]`.

## Check your understanding

1. What values does `range(5, 9)` produce?
2. What is `17 % 5`?
3. What does `lockers_to_check(9, 11)` return?

<details>
<summary>Reveal the practice answers</summary>

1. `5, 6, 7, 8`
2. `2`
3. `[]` — none of 9, 10, or 11 is divisible by 4.

</details>

## Hints for Beacon Checkpoint Scanner

Try the challenge independently first. Open only the next hint if you're stuck.

<details>
<summary>Hint 1 — Which values need to be examined?</summary>

You have two boundaries. Which Python construct will visit each integer once, including the final boundary?

</details>

<details>
<summary>Hint 2 — How do you recognize a qualifying ID?</summary>

Each candidate number must be substituted into **two mathematical expressions**. Use what you know about divisibility and the remainder operator to test the result.

</details>

<details>
<summary>Hint 3 — How do you build the result?</summary>

Make one list before the loop. Add a checkpoint ID to it only when it passes the test. What should be returned when no IDs qualify?

</details>
