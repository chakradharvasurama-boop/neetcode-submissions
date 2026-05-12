# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        li=[]
        curr=head
        while curr:
            li.append(curr)
            curr=curr.next
        l,r=0,len(li)-1
        while r-l>1:
            
            temp=li[l].next
            li[l].next=li[r]
            li[r].next=temp
            l+=1
            r-=1

      
        li[r].next=None
      
   
        


   # [0, 1, 2, 3, 4, 5, 6]


 

        