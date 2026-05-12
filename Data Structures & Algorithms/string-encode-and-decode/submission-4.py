class Solution:

    def encode(self, strs: List[str]) -> str:

        return ''.join([str(len(s))+'#'+s for s in strs])

    def decode(self, s: str) -> List[str]:
   
        i=0
        ans=[]
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            ans.append(s[j+1:j+1+int(s[i:j])])
            i=j+1+int(s[i:j])
        return ans
