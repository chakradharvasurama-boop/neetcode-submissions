class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        ans.append(0)
        curr=1
        for i in range(1,n+1):
            if i&(i-1)!=0:
                t=i>>1
                ans.append(ans[i-curr]+1)
            else:
                ans.append(1)
                curr=i
        print(ans)    
        return ans



        