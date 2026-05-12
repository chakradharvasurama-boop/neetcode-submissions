class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={'{':'}','[':']','(':')'}
        for c in s:
            if c in d:
                stack.append(c)
            elif not len(stack):
                return False  
            else:

                t=stack.pop()
                if d[t]!=c: 
                    return False 
        return not len(stack)  