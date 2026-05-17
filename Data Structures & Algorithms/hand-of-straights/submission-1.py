class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        
        n=len(hand)
        count=n
        hmap={}
        for num in hand:
            hmap[num]=hmap.get(num,0)+1
        currmin=0

        while count:
            currSize=0
            prev=-1
            while currSize<groupSize and count:
                if prev==-1:
                    prev=hand[currmin]
                    count-=1
                    currSize+=1
                    hmap[prev]-=1
                elif prev+1 in hmap and hmap[prev+1]:
                    prev+=1
                    count-=1
                    currSize+=1
                    hmap[prev]-=1
                else:
                    break
            

            if currSize!=groupSize:
                return False
            while currmin<n and not hmap[hand[currmin]]:
                currmin+=1
      



        
        return True

               



        