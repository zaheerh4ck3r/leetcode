class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)  # Sort the array in descending order
        
        for x in range(len(nums) + 1):  # Try all possible values of x
            count = sum(1 for num in nums if num >= x)  # Count numbers greater than or equal to x
            if count == x:  # If count matches x, it's a special array
                return x
        return -1  # If no such x found, return -1

# Example usage:
sol = Solution()
print(sol.specialArray([3, 5]))  # Output: 2
print(sol.specialArray([0, 0]))  # Output: -1
print(sol.specialArray([0, 4, 3, 0, 4]))  # Output: 3
