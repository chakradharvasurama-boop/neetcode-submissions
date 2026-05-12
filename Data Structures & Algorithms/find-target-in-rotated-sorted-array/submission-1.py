class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:

            m=l+(r-l)//2
     #           t
        #4 5 6 1 2 3
    

            if target<nums[m]:
                if nums[l] < nums[r] or nums[m] <=nums[r] or target>=nums[l]:
                    r=m-1
                else:
                    l=m+1
            elif target>nums[m]:
                if nums[l] < nums[r] or nums[m]>=nums[l] or target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
            else:
                return m
                    

        return -1


     


