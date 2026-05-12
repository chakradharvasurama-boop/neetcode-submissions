class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        curr=[]

        def getSubsets(nums,i)->None:
            if i==n:
                ans.append(curr.copy())
                return

            curr.append(nums[i])
            getSubsets(nums,i+1)

            curr.pop()
            getSubsets(nums,i+1)

        getSubsets(nums,0)
        return ans


        