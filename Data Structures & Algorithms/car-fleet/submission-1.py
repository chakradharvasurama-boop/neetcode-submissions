class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetcount=0
        for i in range(len(position)):
            fleet=False
            for j in range(len(position)):
                if i!=j and position[j]>=position[i] and (target-position[j])/speed[j]>=(target-position[i])/speed[i]:
                    fleet=True
                    break
            if not fleet:
                fleetcount+=1
        return fleetcount