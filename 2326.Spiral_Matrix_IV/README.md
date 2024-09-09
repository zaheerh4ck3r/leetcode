
### Problem Breakdown

You have a matrix with dimensions $m \times n$ and a singly linked list. The goal is to fill the matrix in a spiral order with the values from the linked list.

#### Example

Given:

* $m = 3$, $n = 3$ (Matrix dimensions)
* Linked list: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9

The resulting matrix should look like this:

```lua
[[1, 2, 3],
 [8, 9, 4],
 [7, 6, 5]]
```

### Steps to Solve the Problem

1. **Initialize the Matrix**
2. **Define Boundaries**
3. **Traverse and Fill the Matrix in Spiral Order**
4. **Handle Edge Cases**

### 1. Initialize the Matrix

Create a matrix of size $m \times n$ filled with a placeholder value (e.g., `-1`).

```python
matrix = [[-1] * n for _ in range(m)]
```

For $m = 3$ and $n = 3$, this initializes:

```lua
[[-1, -1, -1],
 [-1, -1, -1],
 [-1, -1, -1]]
```

### 2. Define Boundaries

Set up the boundaries for the traversal:

* `left` (initially 0, leftmost column)
* `right` (initially $n - 1$, rightmost column)
* `top` (initially 0, topmost row)
* `bottom` (initially $m - 1$, bottommost row)

### 3. Traverse and Fill the Matrix

Here’s how you fill the matrix in a spiral order:

#### Spiral Order Traversal

**a. Traverse from Left to Right along the Top Boundary**

1. **Move across the top row from the left boundary to the right boundary.**

```python
for col in range(left, right + 1):
    matrix[top][col] = current.val
    current = current.next
```

After filling the top row, update the `top` boundary:

```python
top += 1
```

**b. Traverse from Top to Bottom along the Right Boundary**

1. **Move down the right column from the top boundary to the bottom boundary.**

```python
for row in range(top, bottom + 1):
    matrix[row][right] = current.val
    current = current.next
```

After filling the right column, update the `right` boundary:

```python
right -= 1
```

**c. Traverse from Right to Left along the Bottom Boundary**

1. **Move across the bottom row from the right boundary to the left boundary.**

```python
for col in range(right, left - 1, -1):
    matrix[bottom][col] = current.val
    current = current.next
```

After filling the bottom row, update the `bottom` boundary:

```python
bottom -= 1
```

**d. Traverse from Bottom to Top along the Left Boundary**

1. **Move up the left column from the bottom boundary to the top boundary.**

```python
for row in range(bottom, top - 1, -1):
    matrix[row][left] = current.val
    current = current.next
```

After filling the left column, update the `left` boundary:

```python
left += 1
```

### 4. Handle Edge Cases

Check boundaries to ensure you’re not filling outside the matrix:

```python
while left <= right and top <= bottom:
    # Fill top row
    for col in range(left, right + 1):
        if cur:
            matrix[top][col] = cur.val
            cur = cur.next
    top += 1

    # Fill right column
    for row in range(top, bottom + 1):
        if cur:
            matrix[row][right] = cur.val
            cur = cur.next
    right -= 1

    # Check if boundaries still make sense
    if top <= bottom:
        # Fill bottom row
        for col in range(right, left - 1, -1):
            if cur:
                matrix[bottom][col] = cur.val
                cur = cur.next
        bottom -= 1

    if left <= right:
        # Fill left column
        for row in range(bottom, top - 1, -1):
            if cur:
                matrix[row][left] = cur.val
                cur = cur.next
        left += 1
```

### Full Solution

Here is the complete Python function for this problem:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        matrix = [[-1] * n for _ in range(m)]
        
        left, right = 0, n - 1
        top, bottom = 0, m - 1
        cur = head
        
        while left <= right and top <= bottom:
            # Fill top row
            for col in range(left, right + 1):
                if cur:
                    matrix[top][col] = cur.val
                    cur = cur.next
            top += 1
            
            # Fill right column
            for row in range(top, bottom + 1):
                if cur:
                    matrix[row][right] = cur.val
                    cur = cur.next
            right -= 1
            
            if top <= bottom:
                # Fill bottom row
                for col in range(right, left - 1, -1):
                    if cur:
                        matrix[bottom][col] = cur.val
                        cur = cur.next
                bottom -= 1
            
            if left <= right:
                # Fill left column
                for row in range(bottom, top - 1, -1):
                    if cur:
                        matrix[row][left] = cur.val
                        cur = cur.next
                left += 1
        
        return matrix
```

### Conclusion

This approach is efficient with a time complexity of $O(m \times n)$, where each cell of the matrix is visited exactly once. The boundaries are managed to ensure the correct spiral order, and edge cases are handled to prevent errors when the matrix is fully populated.
