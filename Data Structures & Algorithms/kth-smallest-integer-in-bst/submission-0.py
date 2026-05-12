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
        def dfs(node:TreeNode,currCount)->int:
            left,right=0,0
            if node.left:
                left=dfs(node.left,currCount)
            if left+currCount+1==k:
                nonlocal ans
                ans=node.val
            if node.right:
                right=dfs(node.right,left+1+currCount)
            return 1+left+right
        dfs(root,0)
        return ans