class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res=[0]*len(temperatures)
        for i in range(len(temperatures)-2,-1,-1):
            j=i+1
            while res[j]!=0 and temperatures[i]>=temperatures[j]:
                j=j+res[j]
            if temperatures[j]>temperatures[i]:
                res[i]=j-i
        return res

        