class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(a,b):
            if b==0:
                return 1
            if b==1:
                return a
            res=helper(a*a,b//2)
            return res if b%2==0 else res*a
        result=helper(x,abs(n))
        return  result if n>=0 else 1/result
        