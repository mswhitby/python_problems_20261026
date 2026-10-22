# Robot Maze Navigator

**25 points**

**CS concepts:** Two-dimensional lists, coordinates, graph search, shortest path

## Scenario

A classroom robot moves across a grid with obstacles. To conserve battery power, it must take as few moves as possible to reach a charging station. It might need to explore more than one direction to find the shortest route.

## Parameters

- `grid`: a nonempty rectangular list of lists containing `0` (open floor) and `1` (wall), with at most 12 rows and 12 columns.
- `start` and `target`: `(row, column)` tuples referring to valid open cells in the grid.

## Expected behavior

Return the **minimum number of moves** from `start` to `target`, or `-1` when no route exists. Each move goes one cell up, down, left, or right into an open cell. Diagonal moves and moving through walls are forbidden. Return 0 if `start == target`.

## Your task

Open [`solution.py`](solution.py). Complete the function named `solution` without changing its name or parameters.

```python
def solution(grid, start, target):
    # Write your code here.
```

## Examples

### Example 1

**Input**

```python
solution([[0,0,1],[1,0,0],[0,0,0]], (0,0), (2,2))
```

**Output**

```python
4
```

### Example 2

**Input**

```python
solution([[0,1],[1,0]], (0,0), (1,1))
```

**Output**

```python
-1
```

### Example 3

**Input**

```python
solution([[0]], (0,0), (0,0))
```

**Output**

```python
0
```

Return the required value rather than printing it.
