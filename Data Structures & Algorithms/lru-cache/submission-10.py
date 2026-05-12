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
        self.start=Node(0,0)
        self.last=Node(0,0)
        self.start.next=self.last
        self.last.prev=self.start

    def insert(self,node:Node):
        prev,nxt=self.last.prev,self.last
        prev.next=node
        nxt.prev=node
        node.next=nxt
        node.prev=prev
    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev

        

    def get(self, key: int) -> int:
        #print("get",key)
        if key not in self.hm:
            return -1
        
        #print(self.start.next.val)
        self.remove(self.hm[key])
        self.insert(self.hm[key])
       
        
        

        return self.hm[key].val
        

    def put(self, key: int, value: int) -> None:
        #print("put",key,value)
        
        

        if key in self.hm:
            self.remove(self.hm[key])     
        
        self.hm[key]=Node(key,value)
        self.insert(self.hm[key])
        #print(self.start.next.key)
 
        if len(self.hm)>self.capacity:
            lru=self.start.next
            self.remove(lru)
            del self.hm[lru.key]
        #print(self.start.next.key)
     



       
     
        
        
