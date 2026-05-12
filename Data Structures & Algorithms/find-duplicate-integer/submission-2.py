class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        m=len(nums)+1


        slow,fast=0,0

        slow=nums[slow]
        fast=nums[fast]
        fast=nums[fast]

        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
            fast=nums[fast]
        slow2=0
        
        while slow2 !=slow:
            slow=nums[slow]
            slow2=nums[slow2]

        return slow

        
        


        
        
       

        