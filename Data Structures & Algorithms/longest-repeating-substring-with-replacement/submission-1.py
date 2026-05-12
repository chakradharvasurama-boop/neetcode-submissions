class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #aabbbbcccccdd 2
        #sum=4
        l=len(s)
        ans=1
        for i in range(l):
            currmax=0
            d=defaultdict(int)
            for j in range(i,l):
           
                d[s[j]]+=1
                currmax=max(d[s[j]],currmax)
               
                if(currmax+k>=j-i+1):
                    ans=max(ans,j-i+1)

        return ans


        