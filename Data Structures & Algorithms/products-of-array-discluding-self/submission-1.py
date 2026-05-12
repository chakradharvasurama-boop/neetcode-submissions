class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        res=[1]*(len(nums))
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(len(nums)):
            n=len(nums)
            res[n-i-1]=res[n-i-1]*suffix
            suffix*=nums[n-i-1]
        return res
            
        