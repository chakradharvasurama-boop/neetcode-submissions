class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(nums)
        temp=[]
        s=set()
       

        def getCombinations(nums: List[int],target:int,i:int,curr:int)->None:
            
          
            
            if i==n:
                return
            if curr==target:
                s.add(tuple(temp))
           
                return
            if curr>target:
           
                return
            #print(temp)
            getCombinations(nums,target,i+1,curr)
            curr+=nums[i]
            temp.append(nums[i])
            
            #print(temp)
            getCombinations(nums,target,i,curr)
            getCombinations(nums,target,i+1,curr)
            temp.pop()
            curr-=nums[i]
            
        getCombinations(nums,target,0,0)
        return [list(x) for x in s]

        