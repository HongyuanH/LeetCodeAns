from typing import Mapping
from imports import *

class Solution:
    """
    Runtime: 60 ms, faster than 79.73% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    Memory Usage: 15.7 MB, less than 15.73% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Bisection to find roots for each subtrees.
        Note it's easier to split between mid & mid+1, 
        because mid-1 could be -1, which is not a valid index.
        """
        def helper(start, stop):
            if start == stop:
                return None
            mid = int((start + stop) / 2)
            node = TreeNode(nums[mid])
            node.left = helper(start, mid)
            node.right = helper(mid+1, stop)
            return node
        
        return helper(0, len(nums))

if __name__ == "__main__":
    tree = Solution().sortedArrayToBST([-10,-3,0,5,9])
    print(tree.toList())
    tree.draw()