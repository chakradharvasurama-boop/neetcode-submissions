class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=deque()
        result=[]
        n=len(temperatures)
        for i in range(n):
            while stack and stack[-1][0]<=temperatures[n-i-1]:
                stack.pop()
            
            if stack:
                #print(stack[-1])
                result.append(stack[-1][1]-(n-i-1))
            else:
                result.append(0)
            stack.append((temperatures[n-i-1],n-i-1))
        return result[::-1]
