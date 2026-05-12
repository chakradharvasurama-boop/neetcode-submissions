class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ps=[]
        for i in range(len(position)):
            ps.append((position[i],speed[i]))
        ps.sort()
        count=0
        while ps:
            count+=1
            p,s=ps.pop()
            time=(target-p)/s

            while ps and (target-ps[-1][0])/ps[-1][1]<=time:
                ps.pop()
        
        return count
        

        