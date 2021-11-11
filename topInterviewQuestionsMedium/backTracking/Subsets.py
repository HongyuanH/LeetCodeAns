from imports import *

class Solution:
    """
    Runtime: 32 ms, faster than 84.48% of Python3 online submissions for Subsets.
    Memory Usage: 14.5 MB, less than 52.00% of Python3 online submissions for Subsets.
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]
        subs = self.subsets(nums[1:])
        return [[nums[0]] + sub for sub in subs] + subs

if __name__ == "__main__":
    print(Solution().subsets([1,2,3]))