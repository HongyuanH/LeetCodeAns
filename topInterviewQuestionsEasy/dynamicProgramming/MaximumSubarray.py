from imports import *

class Solution:
    """ 

    """

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm, performance not that good...
        Runtime: 772 ms, faster than 37.85% of Python3 online submissions for Maximum Subarray.
        Memory Usage: 28.5 MB, less than 55.83% of Python3 online submissions for Maximum Subarray.
        """
        best_sum = float('-inf')
        current_sum = 0
        for x in nums:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum