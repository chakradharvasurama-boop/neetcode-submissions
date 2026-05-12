class Solution:
    def reverse(self, x: int) -> int:
        Max=2**31-1
        Min=-2**31
     

   
        ans=0
     
        while x!=0:
            digit=int(math.fmod(x,10))
            
            
            if ans>Max//10 or (ans==Max//10 and digit>Max%10):
                return 0
            if ans<Min//10 or (ans==Min//10 and digit<Min%10):
                return 0
        
            
            x=int(x/10)
            ans=ans*10+digit
        
        
        return ans 
        


        