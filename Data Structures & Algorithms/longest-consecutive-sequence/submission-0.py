class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        s=set(nums)
        ans=1
        for num in s:
            if num-1 not in s:
                count=1
                while num+1 in s:
                    count+=1
                    num+=1
                ans=max(count,ans)
        return ans

            
        