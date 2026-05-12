class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hmap=defaultdict(int)
        for bill in bills:
            if bill==5:
                hmap[5]+=1
            elif bill==10:
                if hmap[5]>0:
                    hmap[5]-=1
                    hmap[10]+=1
                else:
                    return False
            else:
                if hmap[10]:
                    bill-=10
                    hmap[10]-=1
                while bill!=5 and hmap[5]:
                    bill-=5
                    hmap[5]-=1
                if bill!=5:
                    return False
        return True
                   
                


        