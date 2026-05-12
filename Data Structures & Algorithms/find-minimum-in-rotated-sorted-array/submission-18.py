class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        currmin=nums[-1]
        while l<=r:
            m=l+(r-l)//2
            if nums[m]>=nums[l]:
                if(nums[l]<=nums[r]):
                    currmin=min(currmin,nums[l])
                    break
                l=m+1
            else:
                r=m-1
                currmin=nums[m]


        return currmin


       # 3 4 5 6 1 2


        