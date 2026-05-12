class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        visited=[0]*n
        def backtrack(x:int,curr:List[int]):

            curr.append(nums[x])
            if len(curr)==n:
                nonlocal ans
                ans.append(curr.copy())
                curr.pop()
                return
            visited[x]=1
            for i in range(n):
                if not visited[i]:
                    backtrack(i,curr)

            visited[x]=0
            curr.pop()
        for i in range(n):
            backtrack(i,[])
        
        return ans


        