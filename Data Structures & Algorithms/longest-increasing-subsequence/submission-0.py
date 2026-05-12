class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        longest=[1 for i in range(n)]
        for i in range(n):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    longest[i]=max(longest[i],1+longest[j])

        return max(longest)


        