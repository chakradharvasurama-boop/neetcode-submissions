class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jumps=0
        maxIndex=0
        currIndex=0
        n=len(nums)
        l=0
        if n==1:
            return 0

        for i,num in enumerate(nums):
            if i>maxIndex:
                jumps+=1
             
                
                for j in range(currIndex,i):
                    maxIndex=max(maxIndex,j+nums[j])
                currIndex=i-1
            #print(i,currIndex,jumps)
                
                
                    

        return jumps

        