class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        temp=1<<31
        curr=1
        for i in range(32):
            if curr&n:
                ans+=temp
            temp>>=1
            curr<<=1
        return ans

        