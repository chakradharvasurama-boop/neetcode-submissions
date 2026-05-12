class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(nums)
        temp=[]
        #s=set()
       

        def getCombinations(nums: List[int],target:int,i:int,curr:int)->None:
            
            if curr==target:
                #print(temp)
                ans.append(temp.copy())
           
                return
            
            if i==n or curr>target:
                return
      
            #print(temp)
            getCombinations(nums,target,i+1,curr)
            curr+=nums[i]
            temp.append(nums[i])
            
            #print(temp)
            getCombinations(nums,target,i,curr)
        
            temp.pop()
            curr-=nums[i]
            
        getCombinations(nums,target,0,0)
        return ans

        