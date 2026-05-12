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

 

    
        adjMap={}
       
    
        def dfs(curr):
            if curr in adjMap:
                return adjMap[curr]
            adjMap[curr]=Node(curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in adjMap:
                    adjMap[curr].neighbors.append(dfs(neighbor))
                else:
                    adjMap[curr].neighbors.append(adjMap[neighbor])
            return adjMap[curr]

      

      
    
        return dfs(node)
            
                
                


        