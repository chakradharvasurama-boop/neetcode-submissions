class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        misses=0
        d=defaultdict(int)
        for c in s1:
            d[c]+=1
            misses+=1

        currMiss=misses
        d2=defaultdict(int)
        l=0
        for i in range(len(s2)):
            c=s2[i]
            if c in d:
                
                d2[c]+=1
                currMiss-=1
               
                    
             
                while d2[c]>d[c]:
                    d2[s2[l]]-=1
                    l+=1
                    currMiss+=1
            else:
                d2=defaultdict(int)
                currMiss=misses
                l=i+1
            #print(c,currMiss) 
            if currMiss==0:
                return True
        return False
        

        