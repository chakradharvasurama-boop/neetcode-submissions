class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        co={'}':'{',']':'[',')':'('}
        for char in s:
            if char in co:
                if not stack or stack[-1]!=co[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack

        