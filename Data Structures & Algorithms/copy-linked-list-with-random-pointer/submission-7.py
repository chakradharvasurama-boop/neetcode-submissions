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
        oldNew=defaultdict(lambda : Node(0))
        oldNew[None]=None
        curr=head
     

        while curr:
 
            oldNew[curr].val=curr.val
            oldNew[curr].next=oldNew[curr.next]
            oldNew[curr].random=oldNew[curr.random]
            curr=curr.next
        
        

   
        return oldNew[head]

        