from imports import *

class Codec:
    """
    Runtime: 128 ms, faster than 60.56% of Python3 online submissions for Serialize and Deserialize Binary Tree.
    Memory Usage: 24.9 MB, less than 7.95% of Python3 online submissions for Serialize and Deserialize Binary Tree.

    TODO: use str instead of list
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return str(None)
        ans = []
        q = deque()
        q.append(root)
        while len(q):
            node = q.popleft()
            if node:
                ans.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append(None)
        # Removing the tailing None(s) is not necessary
        # But this is the LeetCode way to save some space
        while ans and ans[-1] is None:
            del ans[-1]
        return str(ans)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'None':
            return None
        data = eval(data)
        if not len(data) % 2:
            # Make sure the last node has 2 leaves
            data.append(None)
        root = TreeNode(data[0])
        q = deque()
        q.append(root)
        for left, right in zip(data[1::2], data[2::2]):
            node = q.popleft()
            if left is not None:
                node.left = TreeNode(left)
                q.append(node.left)
            if right is not None:
                node.right = TreeNode(right)
                q.append(node.right)
        return root