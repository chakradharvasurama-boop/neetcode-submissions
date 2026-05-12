class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,l2=len(s1),len(s2)
        a1,a2=[0]*26,[0]*26

        for i in range(l1):
            a1[ord(s1[i])-ord('a')]+=1
        
        h1=','.join([str(x) for x in a1])
        left=0
        for i in range(l2):
            a2[ord(s2[i])-ord('a')]+=1
            if i-left+1==l1:
                if h1==','.join(str(x) for x in a2):
                    return True
                a2[ord(s2[left])-ord('a')]-=1
                left+=1


        
        return False

        