# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()

        t1,t2=l1,l2
        carry=0
        temp=dummy
        while t1 and t2:
            s=t1.val+t2.val+carry
            carry=s//10
            s=s%10
            temp.next=ListNode(s)
            t1=t1.next
            t2=t2.next
            temp=temp.next

        while t1:
            s=t1.val+carry
            carry=s//10
            s=s%10
            temp.next=ListNode(s)
            t1=t1.next
            temp=temp.next
        while t2:
            s=t2.val+carry
            carry=s//10
            s=s%10
            temp.next=ListNode(s)
            t2=t2.next
            temp=temp.next

        if carry:
            temp.next=ListNode(carry)
        return dummy.next




        