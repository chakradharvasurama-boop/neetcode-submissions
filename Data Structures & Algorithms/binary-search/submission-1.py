import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        l,r=0,len(nums)-1
        while l<=r:
            m=l+((r-l)//2)
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                return m
        retrn -1
        """
        index=bisect.bisect_left(nums,target)
        return index if index<len(nums) and nums[index]==target else -1
        
            
        