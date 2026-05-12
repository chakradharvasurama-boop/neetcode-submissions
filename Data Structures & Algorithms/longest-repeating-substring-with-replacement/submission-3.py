class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #aabbbbcccccdd 2
        #sum=4
        l=0
        ans=1
        d=defaultdict(int)
        currmax=0
        currCount=0

        

        for i in range(len(s)):
            d[s[i]]+=1
            currCount+=1
            currmax=max(d.values())
            while(currmax+k<currCount):
                currCount-=1
                
                d[s[l]]-=1
                l+=1
                currmax=max(d.values())

            ans=max(currCount,ans)
            
        return ans


        