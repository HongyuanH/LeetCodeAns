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

    def subsetsWithDup(self, nums):
        """
        Subsets II, no duplicate subsets.
        Simple classic backtracking algorithm with DFS.
        https://leetcode.com/problems/subsets/discuss/429534/General-Backtracking-questions-solutions-in-Python-for-reference-%3A
        """
        ans = []
        nums.sort()
        def dfs(loc, path):
            ans.append(path)
            for i in range(loc, len(nums)):
                if i != loc and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path+[nums[i]])
        dfs(0, [])
        return ans

if __name__ == "__main__":
    print(Solution().subsetsWithDup([1,2,2]))