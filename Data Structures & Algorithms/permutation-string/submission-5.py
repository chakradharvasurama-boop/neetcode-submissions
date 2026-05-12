class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        matches=0

        
        d1,d2=[0]*26,[0]*26

        for i in range(len(s1)):
            d1[ord(s1[i])-ord('a')]+=1
            d2[ord(s2[i])-ord('a')]+=1
        for i in range(26):
            matches+=d1[i]==d2[i]
        
        n=len(s1)
        for i in range(len(s1),len(s2)):
            if matches==26:
                return True
            left=ord(s2[i-n])-ord('a')
            curr=ord(s2[i])-ord('a')
            d2[left]-=1
            if d2[left]==d1[left]:
                matches+=1
            elif d2[left]+1==d1[left]:
                matches-=1
            d2[curr]+=1
            if d2[curr]==d1[curr]:
                matches+=1
            elif d2[curr]-1==d1[curr]:
                matches-=1
            
            

       
        return matches==26
        

        