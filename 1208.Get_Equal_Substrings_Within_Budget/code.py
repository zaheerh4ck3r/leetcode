class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        # Initialize variables
        max_length = 0
        window_start = 0
        current_cost = 0
        
        # Iterate through the strings using sliding window technique
        for window_end in range(len(s)):
            # Calculate the cost of changing the characters
            current_cost += abs(ord(s[window_end]) - ord(t[window_end]))
            
            # If the current cost exceeds maxCost, move the window start
            while current_cost > maxCost:
                current_cost -= abs(ord(s[window_start]) - ord(t[window_start]))
                window_start += 1
            
            # Update max_length if the current window length is greater
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length
