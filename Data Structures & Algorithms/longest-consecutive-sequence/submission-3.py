class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        s=set(nums)
        ans=0
        for num in nums:
            if num+1 not in s:
                count=1
                curr=num
                while curr-1 in s:
                    curr-=1
                    count+=1
                ans=max(count,ans)
          
       
        return ans
            
             

        