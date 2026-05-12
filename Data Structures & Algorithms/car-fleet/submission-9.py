class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeMap={}
        times=[]
        for i in range(len(position)):
            timeMap[position[i]]=(target-position[i])/speed[i]
        for i in range(target):
            if i in timeMap:
                times.append(timeMap[i])
        count=0
        while times:
            count+=1
            t=times.pop()
            while times and times[-1]<=t:
                times.pop()
        
        return count
        

        