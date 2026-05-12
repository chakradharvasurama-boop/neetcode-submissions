class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        ans.append(0)
   
        for i in range(1,n+1):
      
             ans.append(ans[i>>1]+(i&1))
      
           
        print(ans)    
        return ans



        