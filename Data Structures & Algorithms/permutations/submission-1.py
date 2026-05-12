class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        
        def backtrack(i):
            if i==len(nums):
                return [[]]
            perms=backtrack(i+1)
            currRes=[]
            for p in perms:
                for j in range(len(p)+1):
                    pcopy=p.copy()
                    pcopy.insert(j,nums[i])
                    currRes.append(pcopy)
            return currRes



        
        return backtrack(0)


        