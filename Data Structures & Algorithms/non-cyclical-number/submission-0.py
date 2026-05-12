class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True

        seen=set()
     

        while n not in seen and n!=1:
            seen.add(n)
            s=0
            while n!=0:
                t=n%10
                s+=t*t
                n//=10

            n=s
        return n==1
        