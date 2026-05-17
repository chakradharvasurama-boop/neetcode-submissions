class Solution:
    def checkValidString(self, s: str) -> bool:

        n=len(s)
        stack=deque()
        stack2=deque()
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)


            elif c==')':
                if not stack:
                    if stack2:
                        stack2.pop()
                        continue

                    return False
                stack.pop()
            else:
                stack2.append(i)
        while stack:
            if not stack2:
                return False
            if stack2[-1]<stack[-1]:
                return False
            stack2.pop()
            stack.pop()
        
        return True




                

        