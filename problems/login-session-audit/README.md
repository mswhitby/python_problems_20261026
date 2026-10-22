# Login Session Audit

**25 points**

**CS concepts:** State machines, dictionaries, event processing, elapsed-time arithmetic

## Scenario

An app stores a stream of login and logout events. Multiple people can be logged in at the same time, and the same person may return later. The analyst needs to reconstruct completed sessions to calculate active time.

## Parameters

- `events` is a list of dictionaries with the keys `user`, `action`, and `minute`
- `user` (a nonempty string), 
- `action` (`'login'` or `'logout'`) 
- `minute` (a nonnegative integer). Events are in nondecreasing time order; ties are allowed. For any one user, logins and logouts alternate. No logout occurs without a matching earlier login.

## Sample Input

```python
[
    {
        'user':'ava',
        'action':'login',
        'minute':3
    },
    {
        'user':'leo',
        'action':'login',
        'minute':4
    },
    {
        'user':'leo',
        'action':'logout',
        'minute':9
    },
    {
        'user':'ava',
        'action':'logout',
        'minute':11
    }
]
```

## Expected behavior

Return a dictionary mapping each username with **at least one completed session** to their total completed active minutes. A session lasts `logout minute - login minute`; add multiple sessions by the same user. Ignore an unmatched final login. A session lasting zero minutes still counts. Return an empty dictionary if no sessions have completed.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(events):
    # Write your code here.
```

## Examples

```python
solution([{'user':'ava','action':'login','minute':3},{'user':'leo','action':'login','minute':4},{'user':'leo','action':'logout','minute':9},{'user':'ava','action':'logout','minute':11},{'user':'ava','action':'login','minute':12},{'user':'ava','action':'logout','minute':17}])  # {'ava': 13, 'leo': 5}
solution([{'user':'sky','action':'login','minute':2}])  # {}
```

Return the required value rather than printing it.
