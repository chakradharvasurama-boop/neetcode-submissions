# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hmPre={}
        hmIn={}
        n=len(preorder)
        for i in range(n):
            hmPre[preorder[i]]=i
            hmIn[inorder[i]]=i
        

        def construct(i:int,j:int)->TreeNode:
            curr=i
           
            for k in range(i,j+1):
                if hmPre[inorder[k]]<hmPre[inorder[curr]]:
                    curr=k
            
            node=TreeNode(inorder[curr])
            if i<curr:
                node.left=construct(i,curr-1)
            if j>curr:
                node.right=construct(curr+1,j)
            return node
        return construct(0,n-1)



          
         

            

        return construct(0,len(inorder)-1)
            

        