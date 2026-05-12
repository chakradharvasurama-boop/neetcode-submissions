class ListNode:
    def __init__(self,key=0,value=0):
        self.prev=None
        self.next=None
        self.key=key
        self.value=value
        self.d={}
class LRUCache:

    def __init__(self, capacity: int):
        self.d={}
        self.capacity=capacity
        self.head=None
        self.tail=self.head
        
    def makePriority(self,key):
        if len(self.d)!=1:
            
            temp=self.d[key]
            if self.head==temp:
                self.head=self.head.next

            if self.tail!=temp:

                p=temp.prev
                n=temp.next
                if n:
                    n.prev=p
                if p:
                    p.next=n
            
                temp.prev=self.tail
                temp.next=None
                self.tail.next=temp
                self.tail=temp

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        
        self.makePriority(key)


        
        return self.d[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.makePriority(key)
            self.d[key].value=value
            return
        if len(self.d)==self.capacity:
            temp=self.head
            self.d.pop(self.head.key)
            if self.tail==self.head:
                self.tail=self.tail.next
            self.head=self.head.next
            del temp

            

        

        self.d[key]=ListNode(key,value)
        if self.head==None:
            self.head=self.d[key]
            self.tail=self.d[key]
            return
        
        self.tail.next=self.d[key]
        self.d[key].prev=self.tail
        self.tail=self.d[key]
    


        
#2 1

        
       
      

        
