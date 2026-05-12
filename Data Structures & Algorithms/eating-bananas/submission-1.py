import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        ans=r
        while l<=r:
            m=l+(r-l)//2
            currHours=0
            for pile in piles:
                currHours+=math.ceil(pile/m)
            if(currHours<=h):
                r=m-1
                ans=m
            else:
                l=m+1
        return ans
        