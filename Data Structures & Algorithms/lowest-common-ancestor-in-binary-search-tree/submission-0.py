# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        ans=None
        def find(node:TreeNode)->List:
            if node==None:
                return [False,False]
            curr=[False,False]

            if node.val==p.val:
                curr[0]=True

            if node.val==q.val:
                curr[1]=True
            c1=[False,False]
            c2=[False,False]
            if node.left:
                c1=find(node.left)
            if node.right:
                c2=find(node.right)
            curr=[curr[0]or c1[0]or c2[0],curr[1]or c1[1]or c2[1]]
            if curr[0] and curr[1]:
                nonlocal ans
                if ans==None:
                    ans=node
            return curr
        find(root)

        return ans if ans else TreeNode()

            

            
            

            

            

        