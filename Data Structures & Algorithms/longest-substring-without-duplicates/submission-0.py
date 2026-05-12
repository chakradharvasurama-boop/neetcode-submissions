class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        l=0
        ans=0
        for i in range(len(s)):
            if s[i] in se:
                while s[l]!=s[i]:
                    se.remove(s[l])
                    l+=1
                l+=1
            ans=max(i-l+1,ans)
            
            se.add(s[i])

        return ans
        