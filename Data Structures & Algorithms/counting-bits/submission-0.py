class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(0,n+1):
            c=0
            while i!=0:
                i&=i-1
                c+=1
            ans.append(c)
        return ans


        