class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        fleetcount=0
        pairs=[(position[i],(target-position[i])/speed[i]) for i in range(len(position))]
        pairs.sort(reverse=True)
        currGT=0
        for pair in pairs:
            if currGT<pair[1]:
                fleetcount+=1
                currGT=pair[1]
        return fleetcount
        """
        pairs=[(position[i],(target-position[i])/speed[i]) for i in range(len(position))]
        pairs.sort(reverse=True)
        s=deque()
        for pair in pairs:
            if not s:
                s.append(pair)
            else:
                if s[-1][1]<pair[1]:
                    s.append(pair)
        return len(s)
    