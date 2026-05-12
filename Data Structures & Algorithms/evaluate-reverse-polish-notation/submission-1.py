
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations={'+','-','*','/'}
        def perform(a: int , b:int,x: str)->int:
            if x=='+':
                return a+b
            if x=='-':
                return a-b
            if x=='/':
                #print(a,b,val,a//b)
                if(a*b<0):
                    return -1*(abs(a)//abs(b))
                else:
                    return a//b
            return a*b
        stack=deque()
        for val in tokens:
            if val in operations:
                b=stack.pop()
                a=stack.pop()
                stack.append(perform(a,b,val))
               
            else:
                stack.append(int(val))
            #print(val,stack[-1])
            
        
        return stack[-1]


        