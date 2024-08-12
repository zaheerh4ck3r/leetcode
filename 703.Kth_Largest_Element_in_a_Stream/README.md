```python
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap)>k:
        	heapq.heappop(self.minHeap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap) > self.k:
	        heapq.heappop(self.minHeap)
	return self.minHeap[0]

```
### Explanation of the `KthLargest` Class

#### 1. **Initialization (`__init__` method)**:
   - The constructor initializes the class with two parameters: `k` (an integer) and `nums` (a list of integers).
   - The goal is to maintain a min-heap of size `k` that stores the k largest elements encountered so far.
   - **Heap Creation**:
     - `self.minHeap` is initialized with the elements from `nums`.
     - The `heapq.heapify(self.minHeap)` function transforms the list into a min-heap in O(n) time, where `n` is the size of `nums`.
     - The while loop ensures that the heap size is reduced to `k` by repeatedly removing the smallest element using `heapq.heappop(self.minHeap)` until the heap size equals `k`.
     - This process guarantees that only the k largest elements are kept in the heap, with the smallest of these elements at the root.

#### 2. **Add Method (`add` method)**:
   - The `add` method is used to insert a new value `val` into the data stream and return the k-th largest element.
   - **Heap Insertion**:
     - The value `val` is added to the heap using `heapq.heappush(self.minHeap, val)`.
     - If the heap size exceeds `k`, the smallest element (at the root) is removed using `heapq.heappop(self.minHeap)`.
     - This maintains the heap's size at exactly `k`, ensuring that the smallest element in the heap is always the k-th largest in the entire data stream.
   - **Return Value**:
     - The method returns `self.minHeap[0]`, which is the smallest element in the heap, and thus the k-th largest element overall.

