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
        def dfs(node:TreeNode,left,right)->bool:
            if node.val<=left or node.val>=right:
                return False
            valid=True
            if node.left:
                valid =valid and dfs(node.left,left,node.val)

            if node.right:
                valid =valid and dfs(node.right,node.val,right)
            

            return valid



        return dfs(root,float("-inf"),float("inf"))

        
        