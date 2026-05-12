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
        msum=[root.val]
    

        def dfs(node):
            if node==None:
                return 0

            l=dfs(node.left)
            r=dfs(node.right)
       
            msum[0]=max(msum[0],l+r+node.val)
            return max(0,l+node.val,r+node.val)
        dfs(root)
        return msum[0]

        