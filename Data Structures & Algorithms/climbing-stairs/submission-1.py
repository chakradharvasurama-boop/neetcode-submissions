class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n

        twoB,oneB=1,2
       
        curr=0
        for i in range(3,n+1):
            curr=twoB+oneB
            twoB=oneB
            oneB=curr
          
        return curr
        
        
        



        