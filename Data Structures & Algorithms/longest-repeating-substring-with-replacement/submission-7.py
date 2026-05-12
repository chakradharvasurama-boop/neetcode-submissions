class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        d=defaultdict(int)
        n=len(s)
        
        currsize=0
        ans=0
        for c in s:
            d[c]+=1
            m=max(d.values())

            currsize+=1
            if currsize-m>k:
                d[s[l]]-=1
                currsize-=1
                l+=1
            ans=max(currsize,ans)
        return ans
            



        