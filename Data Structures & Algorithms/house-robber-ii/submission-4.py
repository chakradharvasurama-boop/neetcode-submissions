class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
    
        

        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
       

        def helper(i,j):
            dp=nums.copy()
           
            rob1,rob2=0,0
            for k in range(i,j+1):
                r=max(rob1+nums[k],rob2)
                rob1=rob2
                rob2=r
            return rob2

        
        return max(helper(0,n-2),helper(1,n-1))

        