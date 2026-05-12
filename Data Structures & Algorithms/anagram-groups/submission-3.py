class Solution:


    
    def hash(self,s:str)->tuple:
        l=[0]*26
        for c in s:
       
            l[ord(c)-ord('a')]+=1


        
        return tuple(l)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        d={}
        for s in strs:
       
            h=self.hash(s)
   
            if h in d:
                d[h].append(s)
            else:
                d[h]=[s]
        for k in d:
        
            ans.append(d[k])
        return ans


        