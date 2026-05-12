class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        n=len(gas)
        l,r=0,1%n

        
        gasRemaining=gas[0]-cost[0]
        while l!=r:
            
            #print(l,r,gasRemaining)
            while gasRemaining<0:
           
                gasRemaining=gasRemaining-(gas[l]-cost[l])
                l=(l+1)%n
                    
                #print(gasRemaining)
            gasRemaining=gasRemaining+gas[r]-cost[r]


            r=(r+1)%n
        return l

#gas=[5,8,2,8]
#cost=[6,5,6,6]

      
  


 
        