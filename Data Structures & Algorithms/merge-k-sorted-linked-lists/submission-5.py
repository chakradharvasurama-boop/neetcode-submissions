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

        n=len(lists)
        pq=[]
        for i in range(n):
            if lists[i]!=None:
                
                heapq.heappush(pq,(lists[i].val,i))
        
        if len(pq)==0:
            return None
        
        dummy=ListNode()
        temp=dummy
        
        while pq:
            val,i=heapq.heappop(pq)
            temp.next=lists[i]
            lists[i]=lists[i].next
            temp=temp.next

         
            if lists[i]:
                heapq.heappush(pq,(lists[i].val,i))
        
        return dummy.next
        



        
        

            

        


    

        