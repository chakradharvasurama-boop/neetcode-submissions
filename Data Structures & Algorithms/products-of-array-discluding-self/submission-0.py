class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero=nums.count(0)
        ans=[]
        prod=1
        if zero>1:
            return [0]*len(nums)
        if zero==1:
            
            for num in nums:
                if num!=0:
                    prod*=num
            for num in nums:
                if num==0:
                    ans.append(prod)
                else:
                    ans.append(0)
            return ans
        for num in nums:
            prod*=num
        return [int(prod/num) for num in nums]
            
        