class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            s=set()
            for j in range(i+1,len(nums)):
                if target-nums[j] in s:
                    ans.add((nums[i],target-nums[j],nums[j]))
                s.add(nums[j])
        return list(list(x) for x in ans)
                    

        