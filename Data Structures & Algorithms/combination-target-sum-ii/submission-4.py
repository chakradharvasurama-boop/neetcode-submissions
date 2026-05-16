class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(candidates)
        temp=[]
      
        candidates.sort()
       
        #print(candidates)
        def getCombinations(target:int,i:int,curr:int)->None:

            if curr==target:
                ans.append(temp.copy())
                return
            if i==n or curr>target:
                return
            
            #print(temp,i)
            temp.append(candidates[i])
            getCombinations(target,i+1,curr+candidates[i])
            temp.pop()
            j=i
            while j+1<n and candidates[j]==candidates[j+1]:
                j+=1

            getCombinations(target,j+1,curr)
            
            
        getCombinations(target,0,0)
        return ans
        