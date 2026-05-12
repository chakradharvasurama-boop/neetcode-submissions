class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        currmin=nums[0]
        while l<=r:
            if nums[l] < nums[r]:
                currmin = min(currmin, nums[l])
                break
            m=l+(r-l)//2
            currmin=min(nums[m],currmin)
            if nums[m]<nums[l]:
                
                r=m-1
                
            elif nums[m]>=nums[l]:
                l=m+1
                

        return currmin

 #1 3 3 3
 #3 3 1 3


       # 3 4 5 6 1 2


        