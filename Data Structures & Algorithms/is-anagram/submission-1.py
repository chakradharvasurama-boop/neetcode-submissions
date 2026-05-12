class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        
        for ch in s:

            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        
        
        for ch in t:
            if ch in d:
                d[ch]-=1
                if d[ch]<0:
                    return False
            else:
                return False

        return True if len(s)==len(t) else False
        