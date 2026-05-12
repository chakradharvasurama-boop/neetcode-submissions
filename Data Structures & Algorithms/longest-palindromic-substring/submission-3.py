class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ansl,ansr=0,0
      


        

        def backtrack(i:int)->tuple:

            l=i
            r=i


            while l-1>=0 and r+1<n and s[l-1]==s[r+1]:
                l-=1
                r+=1
            curr=r-l

            l2=i
            r2=i+1
            if r2<n and s[l2]==s[r2]:
                while l2-1>=0 and r2+1<n and s[l2-1]==s[r2+1]:
                    l2-=1
                    r2+=1
                if curr<r2-l2:
                    return l2,r2
            return l,r


            
            
        for i in range(n):
            currl,currr=backtrack(i)
            if ansr-ansl<currr-currl:
                ansl,ansr=currl,currr

            
        
       
        return s[ansl:ansr+1]





        