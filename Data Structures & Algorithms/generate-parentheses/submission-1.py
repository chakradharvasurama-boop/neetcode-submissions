class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans=[]
        stack=deque()
        def generate(op,cl,stack):
            if(op<n):
                stack.append('(')
                generate(op+1,cl,stack)
                stack.pop()
            if(cl<op):
                stack.append(')')
                generate(op,cl+1,stack)
                stack.pop()
            if(op==n and cl==n):
                ans.append(''.join(stack))
        generate(0,0,stack)
        return ans
        
        





        