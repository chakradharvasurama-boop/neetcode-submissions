class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps=0
        lastMaxJump=0
        farthest=0
    
        n=len(nums)
        l=0
   

        for i,num in enumerate(nums):
            farthest=max(farthest,i+nums[i])
            if i==lastMaxJump and i!=n-1:
                jumps+=1
                lastMaxJump=farthest
             
                
            
          
                
                
                    

        return jumps

        