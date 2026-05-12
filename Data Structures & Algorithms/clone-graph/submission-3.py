"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==None:
            return

        queue=deque()
 
        queue.append(node)
    
        adjMap={}
       
        adjMap[node]=Node(node.val)

      

        while queue:
            top=queue.popleft()
            
            

            for neighbor in top.neighbors:
             
                if neighbor not in adjMap:
                    adjMap[neighbor]=Node(neighbor.val)
                    queue.append(neighbor)

                adjMap[top].neighbors.append(adjMap[neighbor])
                
             
            
   
        return adjMap[node]
            
                
                


        