# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
       
    

        def dfs(node):
            if node==None:
                return 0,float('-inf')

            l,lmsum=dfs(node.left)
            r,rmsum=dfs(node.right)
    
            msum=max(lmsum,rmsum,l+r+node.val)
            return max(0,l+node.val,r+node.val),msum
        csum,msum=dfs(root)
        
        return msum

        