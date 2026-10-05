"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldnew = {None: None}
        
        curr = head
        while curr:
            oldnew[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldnew[curr]
            copy.next = oldnew[curr.next]
            copy.random = oldnew[curr.random]
            curr = curr.next

        return oldnew[head]
            