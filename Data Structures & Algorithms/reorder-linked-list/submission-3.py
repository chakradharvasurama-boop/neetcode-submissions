# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        
        
        while slow:
            next=slow.next
            slow.next=prev
            prev=slow
            slow=next
        first,second=head,prev

        while first and second:
            temp1,temp2=first.next,second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2


        


        



        












        



        