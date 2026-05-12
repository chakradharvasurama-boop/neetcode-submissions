# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        temp=head
        for _ in range(n):
            temp=temp.next
        prev=None
        curr=head
        while temp:
            temp=temp.next
            prev=curr
            curr=curr.next
        next=curr.next
        if prev:
            print(prev.val)
            prev.next=next
        print(curr.val)
        
        curr.next=None

        return head if curr!=head else next


        