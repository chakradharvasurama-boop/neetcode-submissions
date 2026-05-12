# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        l=[]

        def dfs(node:Optional[TreeNode]):
            if node==None:
                l.append('N')
                return
            l.append(str(node.val))
            dfs(node.left)
            
            dfs(node.right)
        dfs(root)
        return ','.join(l)



      
            





        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=='':
            return None
        #print(data)
        l=data.split(',')
        n=len(l)
        i=0

        def dfs()->Optional[TreeNode]:

            nonlocal i
            if l[i]=='N' or i>=n:
                return None
            
            node=TreeNode(int(l[i]))
            
            
            if l[i+1]=='N' and l[i+2]=='N':
                i+=2
                return node
            i+=1
            node.left=dfs()
            i+=1
            node.right=dfs()
            return node
          
            



            
            
 

        return dfs()




