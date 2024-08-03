```python3
class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        return sorted(target) == sorted(arr)
```
## Step-by-Step Explanation

### Method Definition:
- The `canBeEqual` method takes two parameters: `target` and `arr`, both of which are lists of integers.
- The method returns a boolean value indicating whether `arr` can be transformed to match `target` by reversing subarrays.

### Sorting:
- The method sorts both `target` and `arr` using the `sorted()` function.
- Sorting ensures that if both arrays contain the same elements, regardless of order, they will match after sorting.

### Comparison:
- The sorted versions of `target` and `arr` are compared.
- If the sorted arrays are equal, it means `arr` can be rearranged (by reversing subarrays) to match `target`, and the method returns `True`.
- If they are not equal, the method returns `False`, indicating that it is impossible to make `arr` equal to `target`.

### Key Points:

#### Sorting:
- Sorting both arrays ensures that the order of elements does not matter. We only care about whether both arrays contain the same elements with the same frequencies.
- The time complexity of sorting is `O(n log n)`, where `n` is the length of the arrays. This is efficient and suitable for the given problem constraints.

#### Equality Check:
- After sorting, the equality check is performed in `O(n)` time.
