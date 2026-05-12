class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for string in strs:
            alphabets=[0]*26
            for char in string:
                alphabets[ord(char)-ord('a')]+=1
            alphaCountStr=','.join(str(x) for x in alphabets)
            if alphaCountStr in d:
                d[alphaCountStr].append(string)
            else:
                d[alphaCountStr]=[string]
        ans=[]
        for value in d.values():
            ans.extend([value])
        return ans

        