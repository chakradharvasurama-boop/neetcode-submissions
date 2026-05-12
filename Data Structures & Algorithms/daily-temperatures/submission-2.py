class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=deque()
        n=len(temperatures)
        result=[0]*n
        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                index=stack.pop()
                #print(index)
                result[index]=i-index

            stack.append(i)
        return result
