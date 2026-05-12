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

              
                if d[stack[-1]]!=c: 
                    return False 
                stack.pop()
        return not len(stack)  