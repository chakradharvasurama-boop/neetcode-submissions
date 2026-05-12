class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        
        for i in range(32):
            bit=(n>>i)&1
            #print(bit,1<<(31-i))
            ans|=(bit<<(31-i))
        return ans

        