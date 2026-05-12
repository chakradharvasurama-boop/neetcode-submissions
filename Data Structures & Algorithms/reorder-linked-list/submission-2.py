# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None:
            return
        stack=deque()
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        
        temp=head
        for i in range(length//2):
            if temp:
                temp=temp.next
            
        while temp:
            stack.append(temp)
            prev=temp
            temp=temp.next
            
        
        temp=head
        while stack and temp:
            top=stack.pop()
            if stack:
                top.next=temp.next
                temp.next=top
                temp=top.next
            else:
                temp.next=top
                top.next=None


        












        



        