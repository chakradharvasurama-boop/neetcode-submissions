class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n=len(nums)
        ans=[]
        visited=[0]*n
        def backtrack(curr:List[int]):

          
            if len(curr)==n:
                nonlocal ans
                ans.append(curr.copy())
                return
           
            for i in range(n):
                if not visited[i]:
                    visited[i]=1
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    visited[i]=0

            

        backtrack([])
        
        return ans