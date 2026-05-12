# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        valid=True
        def dfs(node:TreeNode):
            valid,cmin,cmax=True,node.val,node.val
         
            

            if node.left:
                valid_left,lmin,lmax=dfs(node.left)
                valid=valid and valid_left
                if node.val<=lmax:
                    valid=False
                cmin=lmin
            if node.right:
                valid_right,rmin,rmax=dfs(node.right)
                valid=valid and valid_right
                if node.val>=rmin:
                    valid=False
                cmax=rmax
    
            return valid,cmin,cmax
        return dfs(root)[0]

        
        