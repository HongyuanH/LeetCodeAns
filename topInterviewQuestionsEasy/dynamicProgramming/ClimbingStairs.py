from imports import *

class Solution:
    """ 
    Runtime: 28 ms, faster than 86.29% of Python3 online submissions for Climbing Stairs.
    Memory Usage: 14.2 MB, less than 43.91% of Python3 online submissions for Climbing Stairs.
    """

    def climbStairs(self, n: int) -> int: 
        """
        Only need to store the last 2 values.
        Use 0, 1 to index dp for reduced complexity.
        """
        if n == 1:
            return 1
        dp = [1, 2]
        for i in range(2, n):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
            print(i, dp)
        return dp[1]

    def climbStairsDp(self, n: int) -> int: 
        """
        dp[i] = dp[i-1] + dp[i-2]
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp = [1, 2, 0]
        for i in range(2, n):
            dp[i%3] = dp[(i-1)%3] + dp[(i-2)%3]
            print(i, dp)
        return  dp[i%3]

if __name__ == "__main__": 
    print(Solution().climbStairs(5))