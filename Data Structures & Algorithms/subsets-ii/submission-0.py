class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        curr=[]
        s=set()
        nums.sort()

        def backtrack(i:int):
            if i==n:
                print(curr)
                s.add(tuple(curr))
                return
            backtrack(i+1)
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()
        backtrack(0)
  
        return [list(t) for t in s]
        

        