# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        ans=None
        currans=ans
        curr1,curr2=list1,list2

        while curr1 and curr2:
            if curr1.val <curr2.val:
                if currans is None:
                    currans=ListNode()
                    ans=currans
                    currans.val=curr1.val
                else:
                    currans.next=ListNode()
                    currans.next.val=curr1.val
                    currans=currans.next
                curr1=curr1.next
                
            else:
                if currans is None:
                    currans=ListNode()
                    ans=currans
                    currans.val=curr2.val
                else:
                    currans.next=ListNode()
                    currans.next.val=curr2.val
                    currans=currans.next
                curr2=curr2.next
        while curr1:
            currans.next=ListNode()
            currans.next.val=curr1.val
            currans=currans.next
            curr1=curr1.next

        while curr2:
            currans.next=ListNode()
            currans.next.val=curr2.val
            currans=currans.next
            curr2=curr2.next
        return ans


        