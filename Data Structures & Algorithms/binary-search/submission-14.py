class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        bound=len(nums)
        #Upper bound search
        while l<=r:
            m=l+(r-l)//2
            if nums[m]<=target:
                l=m+1
            elif nums[m]>target:
                bound=min(m,bound)
                r=m-1

        
        return bound-1 if bound and nums[bound-1]==target else -1
        