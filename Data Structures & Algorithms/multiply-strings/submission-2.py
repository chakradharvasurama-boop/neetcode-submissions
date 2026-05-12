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
            mulCarry=0
            addCarry=0
            for j in range(m-1,-1,-1):
                currMul=(c*num1arr[j]+mulCarry)
                mulCarry=currMul//10
                currAdd=(currMul%10 + res[respos]+addCarry)
                res[respos]=currAdd%10
                addCarry=currAdd//10
                respos-=1

            totalCarry=mulCarry+addCarry
            if totalCarry!=0:
                curr=res[respos]+totalCarry
                res[respos]=curr%10
                totalCarry=curr//10
        resStart=0
        while resStart<len(res)-1 and res[resStart]==0:
            resStart+=1
        for i in range(resStart,len(res)):
            finalRes.append(str(res[i]))
        return ''.join(finalRes)




        '''
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
        '''



        