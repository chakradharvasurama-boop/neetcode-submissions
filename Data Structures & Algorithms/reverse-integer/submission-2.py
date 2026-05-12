class Solution:
    def reverse(self, x: int) -> int:
        Max=2**31-1
     

        neg=x<0
        ans=0
        if neg:
            x*=-1
        while x!=0:
            digit=x%10
            
            
            if not neg and (ans>Max//10 or (ans==Max//10 and digit>Max%10)):
                return 0
            if neg and ((ans>Max+1)//10 or (ans==(Max+1)//10 and digit>(Max+1)%10)):
                return 0
        
            
            x//=10
            ans=ans*10+digit
        
        if neg:

            return  -ans if -ans >= -2**31 else 0 
        return ans if ans <=2**31-1 else 0
        


        