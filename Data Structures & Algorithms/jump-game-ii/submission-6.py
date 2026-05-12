class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps=0
        maxIndex=0
        farthest=0
    
        n=len(nums)
        l=0
   

        for i,num in enumerate(nums):
            farthest=max(farthest,i+nums[i])
            if i==maxIndex and i!=n-1:
                jumps+=1
                maxIndex=farthest
             
                
            
          
                
                
                    

        return jumps

        