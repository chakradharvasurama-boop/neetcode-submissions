class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        currmin=nums[0]
        while l<=r:
            m=l+(r-l)//2
            if nums[m]>nums[-1]:
                l=m+1
            elif nums[m]<=nums[-1]:
                r=m-1
                currmin=nums[m]

        return currmin

 #1 3 3 3
 #3 3 1 3


       # 3 4 5 6 1 2


        