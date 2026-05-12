# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t,h=head,head
        while h!=None and t!=None:
            t=t.next
            h=h.next
            if h:
                h=h.next

            if t and t==h:
                return True
        return False
        