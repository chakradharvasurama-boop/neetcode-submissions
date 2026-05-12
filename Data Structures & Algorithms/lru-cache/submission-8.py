class Node:
    def __init__(self, key:int=0,value: int=0):
        self.key=key
        self.val=value
        self.next=None
        self.prev=None
       
    
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hm={}
        self.start=None
        self.last=None
        

    def get(self, key: int) -> int:
        #print("get",key)
        if key not in self.hm:
            return -1
        node=self.hm[key]
        #print(self.start.val)
       
        if self.last!=self.hm[key]:

            if self.hm[key]==self.start:
                self.start=self.start.next
        
            prev=self.hm[key].prev
            next=self.hm[key].next
            if prev:
                prev.next=next
            if next:
                next.prev=prev

            
            self.last.next=self.hm[key]
            self.hm[key].prev=self.last
            self.hm[key].next=None
            self.last=self.hm[key]
        

        return self.hm[key].val
        

    def put(self, key: int, value: int) -> None:
        #print("put",key,value)
        
        

        if key in self.hm:
            self.hm[key].val=value
            if self.last!=self.hm[key]:
                if self.hm[key]==self.start:
                    self.start=self.start.next
            
                prev=self.hm[key].prev
                next=self.hm[key].next
                if prev:
                    prev.next=next
                if next:
                    next.prev=prev
                self.last.next=self.hm[key]
                self.hm[key].prev=self.last
                self.hm[key].next=None
                self.last=self.hm[key]
            return

        
        if len(self.hm)==self.capacity:
            print(self.start.val)

            self.hm.pop(self.start.key)
            if self.capacity==1:
                
                self.start=None
                self.last=None
            elif self.start:
                next=self.start.next
                self.start.next=None
                if next:
                    next.prev=None
                self.start=next

                

        if self.start==None:
            self.start=Node(key,value)
            self.last=self.start
            self.hm[key]=self.start
            return
        else:
            node=Node(key,value)
            self.last.next=node
            node.prev=self.last
            self.last=node
            self.hm[key]=node



       
     
        
        
