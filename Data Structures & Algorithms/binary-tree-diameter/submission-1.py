# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depthDim(self,root: Optional[TreeNode]) -> List:
        if root==None:
            return [0,0]
        depthDimL=self.depthDim(root.left)
        depthDimR=self.depthDim(root.right)
        return [1+max(depthDimL[0],depthDimR[0]),max(depthDimL[0]+depthDimR[0],depthDimL[1],depthDimR[1])]
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.depthDim(root)[1]


        