from imports import *

class Solution:
    """
    Runtime: 32 ms, faster than 73.27% of Python3 online submissions for House Robber.
    Memory Usage: 14.2 MB, less than 77.71% of Python3 online submissions for House Robber.
    """
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max0 = nums[0] # max money W/O robbing house (n-1)
        max1 = max(nums[0], nums[1]) # max money W/ robbing house (n-1) 
        for i in range(2, len(nums)):
            max0, max1 = max(max0, max1), max0+nums[i]
        return max(max0, max1)