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
        curr=head
     

        while curr:
            temp=Node(curr.val)
            oldNew[curr]=temp
            curr=curr.next
        
        for old,new in oldNew.items():
            if old.next:
                new.next=oldNew[old.next]
            if old.random:
                new.random=oldNew[old.random]

   
        return oldNew[head] if head else None

        