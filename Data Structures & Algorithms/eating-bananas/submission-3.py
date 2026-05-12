class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        k=r
        def isPossible(tempk:int)->bool:
            hours=0
            for i in range(len(piles)):
                hours+=math.ceil(piles[i]/tempk)


            return hours<=h
        while l<=r:
            m=l+(r-l)//2
            if isPossible(m):
                k=m
                r=m-1

            else:
                l=m+1
        
        return k



        