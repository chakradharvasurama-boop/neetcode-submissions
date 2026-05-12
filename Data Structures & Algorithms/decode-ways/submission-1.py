class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0 for i in range(n+1)]
        dp[n]=1
        for i in range(n-1,-1,-1):
            if s[i]=='0':
                continue
       
                
            dp[i]+=dp[i+1]
          
            if i+2<=n :
                if s[i]=='1' or (s[i]=='2' and s[i+1]<='6') :
                    dp[i]+=dp[i+2]
            
        


        return dp[0]


        '''

        n=len(s)
        dp=[-1 for i in range(n+1)]
        dp[n]=1
        


        def backtrack(i:int)->int:
            if dp[i]!=-1:
                return dp[i]
         
            


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

        '''

        