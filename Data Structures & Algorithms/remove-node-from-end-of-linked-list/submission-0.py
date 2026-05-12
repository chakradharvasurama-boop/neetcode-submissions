# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=1
        while curr.next:
            count+=1
            curr=curr.next
        
        nFromBed=count-n
        prev=None
        curr=head
        while nFromBed:
            prev=curr
            curr=curr.next
            nFromBed-=1
        if curr==head:
            return head.next
        prev.next=curr.next
        return head
        


      #  1 2 3 4
       # 1 2 3
        

        
        