class Solution:
    def rob(self, nums: List[int]) -> int:

        n=len(nums)
        s=sum(nums)
        dp=[[-1 for i in range(s+1)] for j in range(n+1)]
        if n==1:
            return nums[0]

        def backtrack(pos: int,total:int)->int:
            if pos>=n:
                return total
            if dp[pos][total]!=-1:
                return dp[pos][total]
            
            p1=backtrack(pos+2,total+nums[pos])
            p2=backtrack(pos+3,total+nums[pos])
            dp[pos][total]=max(p1,p2)

            return max(p1,p2)

        
        return max(backtrack(0,0),backtrack(1,0))



        