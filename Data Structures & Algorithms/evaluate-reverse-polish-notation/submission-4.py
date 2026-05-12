class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=deque()
        op={'+','-','*','/'}
        for t in tokens:
            if t in op:
                b=s.pop()
                a=s.pop()
                #print(b,a)
                if t=='+':
                    s.append(a+b)
                elif t=='-':
                    s.append(a-b)
                elif t=='*':
                    s.append(a*b)
                else:
                    if a*b>0:
                        s.append(a//b)
                    else:
                        s.append(math.ceil(a/b))
            else:
                s.append(int(t))
            #print(s[-1])
        return s.pop()


        