class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        n=len(nums)
        dp={}
    
        def backtrack(i:int,s:int):
            if (i,s) in dp:
                return dp[(i,s)]
            if s!=0 and s != total and 2*s==total:
            
                    dp[(i,s)]=True
                    return dp[(i,s)]
            if i==n:
                dp[(i,s)]= False
                return dp[(i,s)]
            
            
            dp[(i,s)]=backtrack(i+1,s+nums[i]) or backtrack(i+1,s)
            return dp[(i,s)]
        return backtrack(0,0)
        