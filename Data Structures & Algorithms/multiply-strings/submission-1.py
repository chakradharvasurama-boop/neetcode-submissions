class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1arr=[int(c) for c in num1]
        num2arr=[int(c) for c in num2]
        m=len(num1arr)
        n=len(num2arr)
        res=[0]*(m+n)
        finalRes=[]
        
        
        for i in range(n-1,-1,-1):
            #print(res)
            respos=len(res)-(n-i)
            c=num2arr[i]
           
            for j in range(m-1,-1,-1):
                digit=c*num1arr[j]
                
                res[respos-1]+=(res[respos]+digit)//10
                res[respos]=(res[respos]+digit)%10
                respos-=1
            #print(res)
                

        resStart=0
        while resStart<len(res)-1 and res[resStart]==0:
            resStart+=1
        for i in range(resStart,len(res)):
            finalRes.append(str(res[i]))
        return ''.join(finalRes)



        