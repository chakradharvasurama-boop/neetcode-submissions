class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        ans,curr=0,0
        l=0
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] >=l:
                    l=d[s[i]]+1

            ans=max(ans,i-l+1)
            d[s[i]]=i

        return ans

        