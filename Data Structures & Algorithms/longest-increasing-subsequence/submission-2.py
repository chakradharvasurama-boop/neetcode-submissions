class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        longest=[0 for i in range(n)]

        def backtrack(i)->int:
            if i==n:
                return 0
            if longest[i]:
                return longest[i]
            longest[i]=1
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    longest[i]=max(longest[i],1+backtrack(j))


      

            
            return longest[i]
        return max([backtrack(i) for i in range(n)])


        