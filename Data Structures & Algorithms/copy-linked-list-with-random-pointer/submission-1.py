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
        li=[]
        new=[]
        numberIndex={}
        curr=head
        prev=None
        while curr:
            li.append(curr)
            temp=Node(curr.val)
            new.append(temp)
            numberIndex[curr]=len(li)-1
            curr=curr.next

        for i in range(len(new)):
            if i+1!=len(new):
                new[i].next=new[i+1]
            if li[i].random:
                new[i].random=new[numberIndex[li[i].random]]
        
        return new[0] if new else None

        