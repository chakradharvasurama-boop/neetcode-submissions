class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        bound=-1
        #Upper bound search
        while l<=r:
            m=l+(r-l)//2
            if nums[m]<target:
                bound=max(m,bound)
                l=m+1
            elif nums[m]>=target:
                
                r=m-1

        
        return bound+1 if bound<len(nums)-1 and nums[bound+1]==target else -1
        