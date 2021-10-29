from imports import *

class Solution:
    """
    Runtime: 44 ms, faster than 80.54% of Python3 online submissions for Validate Binary Search Tree.
    Memory Usage: 16.4 MB, less than 81.18% of Python3 online submissions for Validate Binary Search Tree.
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Use a queue for level order traversal, return False immediately if not a valid BST.
        Need to keep track of the minimum & maximum values in the current subtree.
        """
        if not root:
            return False
        q = deque()
        q.append((root, -sys.maxsize, sys.maxsize))
        while len(q):
            node, min_val, max_val = q.popleft()
            if node.left:
                if node.val <= node.left.val:
                    return False
                if node.left.val <= min_val:
                    return False
                q.append((node.left, min_val, min(max_val, node.val)))
            if node.right:
                if node.val >= node.right.val:
                    return False
                if node.right.val >= max_val:
                    return False
                q.append((node.right, max(min_val, node.val), max_val))
        return True


if __name__ == "__main__":
    root = TreeNode.fromList([120,70,140,50,100,130,160,20,55,75,110,119,135,150,200])
    root.draw()
    print(Solution().isValidBST(root))