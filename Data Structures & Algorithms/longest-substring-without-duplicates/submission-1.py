class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        l=0
        ans=0
        for i in range(len(s)):
            if s[i] in d and d[s[i]]>=l:
    
                l=d[s[i]]+1
            ans=max(i-l+1,ans)
            
            d[s[i]]=i

        return ans
        