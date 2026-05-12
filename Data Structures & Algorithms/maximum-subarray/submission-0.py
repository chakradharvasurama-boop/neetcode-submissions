class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        currsum=0
        for num in nums:
            currsum+=num
            if currsum>ans:
                ans=currsum
            if currsum < 0:
                currsum=0
        return ans
        