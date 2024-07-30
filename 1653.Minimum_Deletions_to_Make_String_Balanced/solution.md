# Explanation of `minimumDeletions` Function

The `minimumDeletions` function calculates the minimum number of deletions required to ensure that all 'b's in a given string appear before any 'a's.

## Code

```python
class Solution(object):
    def minimumDeletions(self, s):
        b_count = 0
        deletions = 0

        for char in s:
            if char == 'b':
                b_count += 1
            else:
                deletions = min(deletions + 1, b_count)
        
        return deletions
```
## Steps and Explanation

### 1. Initialization

- **Variables**:
    - `b_count = 0`: Keeps track of the number of 'b's encountered.
    - `deletions = 0`: Tracks the minimum deletions needed to ensure all 'b's come before any 'a's.

### 2. Iterate Through the String

- **Loop Through Each Character**:
    - `for char in s`: Processes each character in the string `s`.

### 3. Update Counts

- **If Character is 'b'**:
    - Increment `b_count` by 1.

- **If Character is 'a'**:
    - Increment `deletions` by 1.
    - Update `deletions` to be the minimum of `deletions + 1` or `b_count`.

### 4. Return Result

- **Final Calculation**:
    - `return deletions`: Returns the value of `deletions`, representing the minimum deletions required.

## Key Points

- **Time Complexity**: O(n), where `n` is the length of the string. The function processes each character once.
- **Space Complexity**: O(1), as only a few extra variables are used.

The approach efficiently calculates the minimum deletions required by tracking the counts of 'b's and 'a's and ensuring that all 'b's are positioned before any 'a's.

