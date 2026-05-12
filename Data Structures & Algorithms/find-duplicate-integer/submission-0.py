class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)-1
        for num in nums:
            if nums[num%(n+1)]>n:
                return num%(n+1)
            nums[num%(n+1)]+=n+1
        return -1