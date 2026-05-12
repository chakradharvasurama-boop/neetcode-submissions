class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        currmin=nums[0]
        while l<=r:
            m=l+(r-l)//2
            if nums[m]>nums[r]:
                l=m+1
            elif nums[m]<=nums[r]:
                r=m-1
                currmin=min(nums[m],currmin)

        return currmin

 #1 3 3 3
 #3 3 1 3


       # 3 4 5 6 1 2


        