class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        def move(x):
            su=0
            while x!=0:
                t=x%10
                su+=t*t
                x//=10
            return su

        f,s=n,n
        s=move(s)
        f=move(f)
        f=move(f)
        while s!=f:
            s=move(s)
            f=move(f)
            f=move(f)



  



        
        return s==1
        