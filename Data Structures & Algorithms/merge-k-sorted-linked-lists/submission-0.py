# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)
        if n==0:
            return None

        
        ans=ListNode(0)
        for l in lists:

            curr=ans

            while l and curr.next:
                if l.val<=curr.next.val:
                    temp=curr.next
                    curr.next=ListNode(l.val)
                    curr.next.next=temp
                    l=l.next
                else:
                    curr=curr.next

            if l:
                curr.next=l
        return ans.next

        