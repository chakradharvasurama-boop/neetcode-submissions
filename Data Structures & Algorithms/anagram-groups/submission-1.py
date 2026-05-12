class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for string in strs:
            alphabets=[0]*26
            for char in string:
                alphabets[ord(char)-ord('a')]+=1
            alphaCountStr=tuple(alphabets)
        
            d[alphaCountStr].append(string)
 

        return list(d.values())

        