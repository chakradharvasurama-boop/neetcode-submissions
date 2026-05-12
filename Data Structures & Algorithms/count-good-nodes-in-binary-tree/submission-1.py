# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root==None:
            return 0
        q=deque()
        count=0

        q.append((root,root.val-1))

        while q:
            node,greatest=q.popleft()
            if node.val>=greatest:
                count+=1
            greatest=max(node.val,greatest)

            if node.left:
                q.append((node.left,greatest))
            if node.right:
                q.append((node.right,greatest))
        return count





        
        '''
        if root==None:
            return 0
       

        def dfs(node:TreeNode,greatest:int)->int:
            if node==None:
                return 0
            count=0
            if node.val>=greatest:
                count+=1
            greatest=max(node.val,greatest)
            if node.left:
                count+=dfs(node.left,greatest)
            if node.right:
                count+=dfs(node.right,greatest)
            return count




        return dfs(root,root.val-1)
        '''