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
        s=deque()
        node=root
        count=0
        
        while node or s:
            while node:
                s.append(node)
                node=node.left
    
            node=s.pop()
            count+=1
            if count==k:
                return node.val
    
            node=node.right
        return 0