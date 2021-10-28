from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int=0, left: "TreeNode"=None, right: "TreeNode"=None):
        self.val = val
        self.left = left
        self.right = right

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
        l = self.toNestedList()
        return [val for level in l for val in level]

    def draw(self):
        from drawtree import draw_level_order
        draw_level_order(str(self.toList()))
        
    @classmethod
    def fromList(cls, l) -> "TreeNode":
        if not l:
            return None
        def inner(index: int = 0) -> TreeNode:
            if len(l) <= index or l[index] is None:
                return None
            node = TreeNode(l[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node
        return inner()
