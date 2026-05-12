# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def checkSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None and subRoot==None:
            return True
        if root==None or subRoot==None:
            return False
        if root.val!=subRoot.val:
            return False

        return self.checkSame(root.left,subRoot.left) and self.checkSame(root.right,subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root==None and subRoot==None:
            return True
        if root==None or subRoot==None:
            return False
        exist=False
        if root.val==subRoot.val:
            exist=self.checkSame(root,subRoot)
        if not exist:
            exist=self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        return exist


        
        