class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        for num in nums:
            if num in d:
                continue
            d[num]=num

            if num-1 in d:
                d[num-1]=num
            if num+1 in d:
                d[num]=num+1
        ans=0
        for key,value in d.items():
            if key==value:
                count =1
                curr=key
                while curr-1 in d:
                    curr-=1
                    count+=1
                ans=max(count,ans)
        return ans
            
             

        