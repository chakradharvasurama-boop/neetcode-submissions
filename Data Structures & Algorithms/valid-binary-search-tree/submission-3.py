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
        def dfs(node:TreeNode)->List:
            curr=[True,node.val,node.val]
            

            if node.left:
                l=dfs(node.left)
                curr[0]=curr[0] and l[0]
                if node.val<=l[2]:
                    curr[0]=False
                curr[1]=l[1]
            if node.right:
                r=dfs(node.right)
                curr[0]=curr[0] and r[0]
                if node.val>=r[1]:
                    curr[0]=False
                curr[2]=r[2]
            #print(curr)
            return curr



        return dfs(root)[0]
        
        