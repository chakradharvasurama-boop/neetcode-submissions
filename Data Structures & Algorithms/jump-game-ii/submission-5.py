class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps=0
        maxIndex=0
        lastCheckedIndex=0
        n=len(nums)
        l=0
   

        for i,num in enumerate(nums):
            if i==maxIndex and i!=n-1:
                jumps+=1
             
                
                for j in range(lastCheckedIndex,i+1):
                    maxIndex=max(maxIndex,j+nums[j])
                lastCheckedIndex=i
            #print(i,currIndex,jumps)
                
                
                    

        return jumps

        