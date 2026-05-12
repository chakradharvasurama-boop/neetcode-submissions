class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        n=len(gas)
        l=0
        totalgas=0
        for i in range(n):
            totalgas+=gas[i]-cost[i]
            if totalgas<0:
                l=i+1
                totalgas=0
            
            


        
        return l

#gas=[5,8,2,8]
#cost=[6,5,6,6]

      
  


 
        