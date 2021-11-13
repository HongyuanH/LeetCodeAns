from imports import *

class Solution:
    """
    Runtime: 40 ms, faster than 67.97% of Python3 online submissions for Delete Node in a Linked List.
    Memory Usage: 14.9 MB, less than 31.15% of Python3 online submissions for Delete Node in a Linked List.
    
    Interesting problem but not interesting problem.
    """
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next