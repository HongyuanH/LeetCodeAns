from imports import *

class Solution:
    """
    Runtime: 36 ms, faster than 70.47% of Python3 online submissions for Symmetric Tree.
    Memory Usage: 14.3 MB, less than 78.08% of Python3 online submissions for Symmetric Tree.
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Pay attention to the "not left and not right" case.
        This is for checking the leaves.
        """
        if not root:
            return False
        
        def compareTree(left, right):
            if not left and not right:
                return True
            if left and not right:
                return False
            if right and not left:
                return False
            if left.val != right.val:
                return False
            return compareTree(left.left, right.right) and compareTree(left.right, right.left)
        
        return compareTree(root.left, root.right)

if __name__ == "__main__":
    root = TreeNode.fromList([1,2,2,3,4,4,3])
    root.draw()
    print(Solution().isSymmetric(root))