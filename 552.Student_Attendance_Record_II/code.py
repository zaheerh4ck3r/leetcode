class Solution:
    MOD = 1000000000 + 7
    def checkRecord(self,n):
        prevDP = [[1] * 3 for _ in range(2)]

        for i in range(1, n + 1):
            newDP = [[0] * 3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    # Pick P
                    newDP[a][l] += prevDP[a][2]
                    newDP[a][l] %= self.MOD
                    if a > 0:
                        # Pick A
                        newDP[a][l] += prevDP[a - 1][2]
                        newDP[a][l] %= self.MOD
                    if l > 0:
                        # Pick L
                        newDP[a][l] += prevDP[a][l - 1]
                        newDP[a][l] %= self.MOD
            prevDP = newDP

        return prevDP[1][2]
