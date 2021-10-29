from imports import *

class Solution:
    """
    Runtime: 44 ms, faster than 63.78% of Python3 online submissions for Maximum Depth of Binary Tree.
    Memory Usage: 16.1 MB, less than 41.99% of Python3 online submissions for Maximum Depth of Binary Tree.
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Easy to understand...
        Will iterative method save memory?
        """
        if root is not None:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            if leftDepth > rightDepth:
                return leftDepth + 1
            else:
                return rightDepth + 1
        else:
            return 0

if __name__ == "__main__":
    # TODO:
    root = TreeNode.fromList("[3,9,20,null,null,15,7]")
    root.draw()
    print(Solution().maxDepth(root))