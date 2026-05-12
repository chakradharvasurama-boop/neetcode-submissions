# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode()
        temp=ans
        curr1,curr2=l1,l2
        store=0
        while curr1 or curr2:
            if curr1:
                store+=curr1.val
                curr1=curr1.next
            if curr2:
                store+=curr2.val
                curr2=curr2.next
            temp.next=ListNode(store%10)
            temp=temp.next
            store//=10
        if store:
            temp.next=ListNode(store)

        return ans.next


      

              

        