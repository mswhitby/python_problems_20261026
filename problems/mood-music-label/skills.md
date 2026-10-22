# Skills Guide: Mood-to-Music Label

**Optional refresher — not the solution to this challenge.** The examples use a different app feature, so you can learn the Python operations and apply them yourself. Return to [Mood-to-Music Label](README.md) when ready.

## What you'll practice

| Skill | What it does |
|---|---|
| Function parameter | Receives data from the caller |
| String | Stores text between quotes |
| `.strip()` | Removes whitespace from the beginning and end |
| `.title()` | Capitalizes words for display |
| `+` | Joins strings together |
| `return` | Sends the result back to the caller |

## 1. Parameters and strings

A **parameter** is a variable listed in a function definition. Its value comes from the **argument** supplied when calling the function.

```python
def greet(person):
    return 'Hello, ' + person

greet('Alex')  # 'Hello, Alex'
```

Strings are text values. Quotation marks are part of Python's syntax, but they are not characters inside the resulting message.

## 2. Remove extra spaces from the ends

`.strip()` removes spaces and other whitespace from **both ends** of a string.

```python
label = '   science fair   '
clean = label.strip()
print(clean)  # science fair
```

This does **not** remove the space between `science` and `fair`, and it does not automatically remove repeated spaces **inside** the string.

## 3. Make words display consistently

`.title()` makes the first letter of each word uppercase and the remaining letters lowercase.

```python
print('ROBOTICS lab'.title())  # Robotics Lab
print('weekend PROJECT'.title())  # Weekend Project
```

Remember: a string method returns a new string. To use the transformed result, assign or return it.

## 4. Combine strings

The `+` operator joins strings in order. Spaces have to be included explicitly where they belong.

```python
topic = 'Robotics'
heading = topic + ' Workshop'
print(heading)  # Robotics Workshop
```

`' Workshop'` begins with a space. Without that space, the result would be `'RoboticsWorkshop'`.

## 5. Worked example — Label a school workshop

**Different task:** A school app creates display labels for workshop topics. The user may type a topic with extra outer spaces or unusual capitalization. The app should display a neatly capitalized topic followed by ` Workshop`.

```python
def workshop_label(topic):
    cleaned_topic = topic.strip()
    display_topic = cleaned_topic.title()
    result = display_topic + ' Workshop'
    return result
```

**Input**

```python
workshop_label('   ROBOTICS lab  ')
```

**Output**

```python
'Robotics Lab Workshop'
```

### Follow each value

| Step | Value |
|---|---|
| Original parameter | `'   ROBOTICS lab  '` |
| After `.strip()` | `'ROBOTICS lab'` |
| After `.title()` | `'Robotics Lab'` |
| After adding suffix | `'Robotics Lab Workshop'` |

The challenge you were assigned is about naming music sessions, not school workshops. Choose the operations that meet its stated requirements.

## Common mistakes to watch for

- **Using `.strip()` without saving its result:** strings are immutable; the original variable isn't updated automatically.
- **Using `.upper()` for a title:** it makes *every* letter uppercase.
- **Putting the suffix in the wrong place:** a prefix appears before text; a suffix appears after it.
- **Forgetting the separating space:** the required output must match exactly.
- **Printing instead of returning:** the grader checks the value the function returns, not what it prints.
- **Returning an unquoted name:** text values must be strings.

## Check your understanding

1. What does `'  CODE  '.strip()` return?
2. What does `'PYTHON basics'.title()` return?
3. What does `'Game' + ' Night'` return?

<details>
<summary>Reveal the practice answers</summary>

1. `'CODE'`
2. `'Python Basics'`
3. `'Game Night'`

</details>

## Hints for Mood-to-Music Label

Try the challenge before opening hints.

<details>
<summary>Hint 1 — What does the input need first?</summary>

Consider whether the text can have spaces at the very beginning or end. Which string method addresses that?

</details>

<details>
<summary>Hint 2 — How should each word look?</summary>

Compare `.upper()`, `.lower()`, and `.title()`. Which one matches the examples in the challenge?

</details>

<details>
<summary>Hint 3 — What must the function give back?</summary>

Think about where the fixed suffix belongs, how to include the separating space, and why `return` is needed instead of `print`.

</details>
