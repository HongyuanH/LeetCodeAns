from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int=0, left: "TreeNode"=None, right: "TreeNode"=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if self.left and self.right:
            return f"{self.val}, left: {self.left.val}, right: {self.right.val}"
        elif self.left and not self.right:
            return f"{self.val}, left: {self.left.val}, right: None"
        elif not self.left and self.right:
            return f"{self.val}, left: None, right: {self.right.val}"
        else:
            return f"{self.val}, left: None, right: None"

    def toNestedList(self) -> List[List[int]]:
        # FIXME: node == None
        q = deque()
        q.append((self, 0))
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
    
    def toList(self) -> List[int]:
        data = []
        q = deque()
        q.append(self)
        while len(q):
            node = q.popleft()
            if node:
                data.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                data.append(None)
        # Removing the tailing None(s) is not necessary
        # But this is the LeetCode way to save some space
        while data and data[-1] is None:
            del data[-1]
        return data

    def draw(self):
        from drawtree import draw_level_order
        data = str(self.toList()).replace("None", "#").replace(" ", "")
        draw_level_order(data)
    
    @classmethod
    def fromStr(cls, data: str) -> "TreeNode":
        data = data.replace("null", "None")
        data = eval(data)
        return cls.fromList(data)

    @classmethod
    def fromList(cls, data: List[int]) -> "TreeNode":
        if not data:
            return None
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
