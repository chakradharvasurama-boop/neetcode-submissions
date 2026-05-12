# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        dummy=ListNode()
        dummy.next=head
        left=dummy
        temp=head
        for _ in range(n):
            temp=temp.next
   
        while temp and left:
            temp=temp.next
            left=left.next

        left.next=left.next.next
        


        return dummy.next


        