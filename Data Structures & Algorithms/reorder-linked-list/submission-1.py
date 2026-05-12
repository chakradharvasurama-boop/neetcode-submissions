# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
   
        def reverse(head):
            prev=None
            while head:
                temp=head.next
                head.next=prev
                prev=head
                head=temp
            return prev
        def findMiddle(head):
            if head is None:
                return None
            tort,hare=head,head
            while hare and hare.next:
                tort=tort.next
                hare=hare.next.next
            return tort

        middle=findMiddle(head)

        curr1,curr2=head,reverse(middle.next)
        middle.next=None
        while curr2:
            temp1=curr1.next
            temp2=curr2.next
            curr1.next=curr2
            curr2.next=temp1
            curr1=temp1
            curr2=temp2
     



        
        




        
      
   
        


   # [0, 1, 2, 3, 4, 5, 6]

   #0 1 2 3 6 5 
  # 0 5 1 4 2 3




 

        