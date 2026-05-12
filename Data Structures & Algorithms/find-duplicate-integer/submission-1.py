class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        m=len(nums)+1
        for i in range(n):
            nums[nums[i]%m-1]+=m
        for i in range(n):
            if nums[i]//m>1:
                return i+1
        return 0
        


        
        
       

        