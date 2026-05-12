class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        s=set(nums)
        ans=0
        for num in s:
            if num-1 not in s:
                count=1
                while num+1 in s:
                    count+=1
                    num+=1
                ans=max(count,ans)
        return ans

            
        