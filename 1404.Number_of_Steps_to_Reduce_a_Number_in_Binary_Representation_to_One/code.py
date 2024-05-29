class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        steps = 0
        s = list(s)
        
        while len(s) > 1:
            if s[-1] == '0':
                # If the number is even, divide by 2
                s.pop()
            else:
                # If the number is odd, add 1
                # This may cause carry, so handle it
                i = len(s) - 1
                while i >= 0 and s[i] == '1':
                    s[i] = '0'
                    i -= 1
                if i < 0:
                    s.insert(0, '1')
                else:
                    s[i] = '1'
            steps += 1
        
        return steps
