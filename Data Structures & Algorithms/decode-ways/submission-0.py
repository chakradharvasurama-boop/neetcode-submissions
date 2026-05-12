class Solution:
    def numDecodings(self, s: str) -> int:
        curr=[]
        n=len(s)
        dp=[-1 for i in range(n+1)]
        dp[n]=1
        


        def backtrack(i:int)->int:
            if dp[i]!=-1:
                return dp[i]
            if i==n:
                return 1
            


            if s[i]=='0':
                dp[i]=0
                return 0


            count=0

            if i+1<=n:
                
                count+=backtrack(i+1)
          
            if i+2<=n :
                if s[i]=='1' or (s[i]=='2' and s[i+1]<='6') :
                    count+=backtrack(i+2)
          

            dp[i]=count
                
       
            
            return dp[i]
        return backtrack(0)

        