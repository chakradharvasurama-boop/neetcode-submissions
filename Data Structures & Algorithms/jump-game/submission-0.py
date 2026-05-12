class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex=0
        for i,num in enumerate(nums):
            if i>maxIndex:
                return False
            maxIndex=max(maxIndex,i+num)
        return True
        