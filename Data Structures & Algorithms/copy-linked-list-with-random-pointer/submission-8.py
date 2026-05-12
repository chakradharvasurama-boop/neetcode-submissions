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
        oldNew={}
        temp=head
        oldNew[None]=None
        while temp:
            oldNew[temp]=Node(temp.val)
            temp=temp.next

        temp=head
        while temp:
            oldNew[temp].next=oldNew[temp.next]
            oldNew[temp].random=oldNew[temp.random]
            temp=temp.next
        return oldNew[head]

        