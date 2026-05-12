# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#d->1-> 2-> 3-> 4
#d<-1-> 2-> 3-> 4
#d<-1<- 2-> 3-> 4
#4<-1<- 2 <- 3<- d


class Solution:
    def reversePart(self,prev:Optional[ListNode],l:Optional[ListNode],r:Optional[ListNode]):
        #print("Before reverse")
        #curr=l
        #while curr!=r:
        #    print(curr.val)
        #    curr=curr.next
        #print(curr.val)

        #print()
        p=prev
        curr=l
        nxt=r.next
        while  curr!=r:
            temp=curr.next
            curr.next=p
            p=curr
            curr=temp

        curr.next=p

        l.next=nxt
        prev.next=r
        #print("after reverse")
        #curr=r
        #while curr!=l:
        #    print(curr.val)
        #    curr=curr.next
        #print(curr.val)

        #print()
        return r,l

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1 or head==None:
            return head

        
        l,r=head,head
        
        for i in range(k-1):
            r=r.next
            if r==None:
                break
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        while r!=None:
            l,r=self.reversePart(prev,l,r)
            for i in range(k):
                prev=prev.next
                l=l.next
                r=r.next
                if r==None:
                    break
            
        return dummy.next
            
            



        