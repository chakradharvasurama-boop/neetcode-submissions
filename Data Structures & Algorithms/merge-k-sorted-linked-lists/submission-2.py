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
        
        pq=[]
        for node  in lists:
            while node:
                pq.append(node.val)
                node=node.next
        
        heapq.heapify(pq)
        if len(pq)==0:
            return None
        
        ans=ListNode(heapq.heappop(pq))
        temp=ans
        while pq:
            temp.next=ListNode(heapq.heappop(pq))
            temp=temp.next



            
        return ans
        


    

        