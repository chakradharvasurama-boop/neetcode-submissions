class Solution:

    def encode(self, strs: List[str]) -> str:
        temp=[]
        for s in strs:
            l=str(len(s))
            temp.append(l+'-'+s)
        return ''.join(temp)



    def decode(self, s: str) -> List[str]:
  
        i=0
        n=len(s)
        ans=[]
        while i<n:
            curr=i
            while s[i]!='-':
                i+=1
            length=int(s[curr:i])
            if length==0:
                ans.append('')
            else:
                ans.append(s[i+1:i+length+1])
            i=i+length+1



            

        return ans



