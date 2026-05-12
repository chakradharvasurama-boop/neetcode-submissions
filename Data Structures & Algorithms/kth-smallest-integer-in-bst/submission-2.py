# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:
            return 0
        ans=0
        q=deque()
        count=0
        def dfs(node:TreeNode):
            left,right=0,0
            if node.left:
                left=dfs(node.left)
            nonlocal ans,count
            count+=1
            if count==k:
                
                ans=node.val
                return 
            if node.right:
                right=dfs(node.right)
     
        dfs(root)
        return ans