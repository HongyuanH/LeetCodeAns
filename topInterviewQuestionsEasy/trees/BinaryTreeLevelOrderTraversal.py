from imports import *

class Solution:
    """
    Use a queue for level order traversal.
    Need to keep track of the levels for each node.
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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