class Solution:
    def reverse(self, x: int) -> int:
        neg=x<0
        ans=0
        if neg:
            x*=-1
        while x!=0:
            ans*=10
            ans+=x%10
            
            x//=10
        
        if neg:

            return  -ans if -ans >= -2**31 else 0 
        return ans if ans <2**31-1 else 0
        


        