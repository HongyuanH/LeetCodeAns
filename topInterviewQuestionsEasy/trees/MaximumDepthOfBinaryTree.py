from imports import *

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
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