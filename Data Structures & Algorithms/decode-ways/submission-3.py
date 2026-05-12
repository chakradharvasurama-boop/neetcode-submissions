class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        curr,next1,next2=1,0,0
        for i in range(n-1,-1,-1):
            next2=next1
            next1=curr
            curr=0
            if s[i]!='0':   
                curr+=next1
            
                if i+2<=n :
                    if s[i]=='1' or (s[i]=='2' and s[i+1]<='6') :
                        curr+=next2
            
            
        


        return curr


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

        