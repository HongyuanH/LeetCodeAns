from imports import *

class Solution:
    """
    Runtime: 36 ms, faster than 72.58% of Python3 online submissions for Binary Tree Level Order Traversal.
    Memory Usage: 14.4 MB, less than 86.41% of Python3 online submissions for Binary Tree Level Order Traversal.
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Use a queue for level order traversal.
        Need to keep track of the levels for each node.
        """
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        ans = []
        while len(q):
            node, level = q.popleft()
            if level >= len(ans):
                ans.append([])
            ans[level].append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return ans

if __name__ == "__main__":
    # TODO:
    root = TreeNode.fromList("[3,9,20,null,null,15,7]")
    root.draw()
    print(Solution().levelOrder(root))