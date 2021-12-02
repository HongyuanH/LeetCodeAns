class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    """
    Runtime: 36 ms, faster than 81.61% of Python3 online submissions for Clone Graph.
    Memory Usage: 14.4 MB, less than 99.59% of Python3 online submissions for Clone Graph.
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        def dfs(cur_node, visited):
            for neighbor in cur_node.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val)
                    dfs(neighbor, visited)
                visited[cur_node.val].neighbors.append(visited[neighbor.val])
        visited = {node.val: Node(node.val)}
        dfs(node, visited)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

Solution().cloneGraph(node1)