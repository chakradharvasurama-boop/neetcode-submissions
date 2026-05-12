# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None and list2==None:
            return None

        ans=None
        curr=ans

        while list1!=None and list2!=None:
            if list1.val<list2.val:
                if ans==None:
                    ans=ListNode()
                    ans.val=list1.val
                    curr=ans
         
                else:
                    curr.next=ListNode(list1.val)
                    curr=curr.next
                list1=list1.next
            else:
                if ans==None:
                    ans=ListNode()
                    ans.val=list2.val
                    curr=ans
 
                else:
                    curr.next=ListNode(list2.val)
                    curr=curr.next
                list2=list2.next
        
        while list1 !=None:
            if ans==None:
                ans=ListNode()
                ans.val=list1.val
                curr=ans
         
            else:
                curr.next=ListNode(list1.val)
                curr=curr.next
            list1=list1.next
        while list2 !=None:
            if ans==None:
                ans=ListNode()
                ans.val=list2.val
                curr=ans
         
            else:
                curr.next=ListNode(list2.val)
                curr=curr.next
            list2=list2.next
        return ans

                


        

        