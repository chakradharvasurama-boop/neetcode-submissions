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
        hmap={}
        n=len(lists)
        pq=[]
        for i in range(n):
            if lists[i]!=None:
                hmap[i]=lists[i]
                heapq.heappush(pq,(lists[i].val,i))
        
        if len(pq)==0:
            return None
        
        dummy=ListNode()
        temp=dummy
        while pq:
            val,indx=heapq.heappop(pq)
            temp.next=ListNode(val)
            temp=temp.next

            hmap[indx]=hmap[indx].next
            if hmap[indx]:
                heapq.heappush(pq,(hmap[indx].val,indx))
        
        return dummy.next
        



        
        

        
      



            
        return ans
        


    

        