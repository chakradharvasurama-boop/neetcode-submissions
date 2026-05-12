class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,l2=len(s1),len(s2)
        if(l1>l2):
            return False
        a1,a2=[0]*26,[0]*26

        for i in range(l1):
            a1[ord(s1[i])-ord('a')]+=1
            a2[ord(s2[i])-ord('a')]+=1
        matches=0
        for i in range(26):
            matches+=1 if a1[i]==a2[i] else 0
        
       
        left=0
        for i in range(l1,l2):
            if matches==26:
                break
            index=ord(s2[i])-ord('a')
            a2[index]+=1
            if a1[index]==a2[index]:
                matches+=1
            elif a1[index]==a2[index]-1:
                matches-=1

            index=ord(s2[left])-ord('a')
            a2[index]-=1
            if a1[index]==a2[index]:
                matches+=1
            elif a1[index]==a2[index]+1:
                matches-=1
            left+=1



        
        return matches==26

        