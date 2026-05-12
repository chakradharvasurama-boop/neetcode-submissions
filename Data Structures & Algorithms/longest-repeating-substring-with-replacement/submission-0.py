class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #aabbbbcccccdd 2
        #sum=4
        l=len(s)
        ans=1
        for i in range(l):
            for j in range(i+1,l):
                currmax=0
                d=defaultdict(int)
                for p in range(i,j+1):
                    d[s[p]]+=1
                    currmax=max(d[s[p]],currmax)
               
                if(currmax+k>=j-i+1):
                    ans=max(ans,j-i+1)

        return ans


        