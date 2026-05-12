class Solution:
    def rob(self, nums: List[int]) -> int:

        n=len(nums)
        s=sum(nums)
        dp=[-1 for i in range(n)]
    
        if n==1:
            return nums[0]

        def backtrack(pos: int)->int:
            if pos>=n:
                return 0
            if dp[pos]!=-1:
                return dp[pos]
           
            
            p1=backtrack(pos+1)
            p2=nums[pos]+backtrack(pos+2)
            dp[pos]=max(p1,p2)

            return dp[pos]

        
        return backtrack(0)



        