class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t)>len(s):
            return ""
        d1=defaultdict(int)
        d2=defaultdict(int)
        for i in  range(len(t)):
            d1[t[i]]+=1
        have,need=0,len(d1)
        anslen=len(s)+1
        ansl,ansr=-1,-1
        left=0
        for i in range(len(s)):
            d2[s[i]]+=1
            if s[i] in d1 and d1[s[i]]==d2[s[i]]:
                have+=1
            
            while have==need:   
                
                if i-left+1<anslen:
                    anslen=i-left+1
                    ansl,ansr=left,i
                d2[s[left]]-=1
                if s[left] in d1 and d2[s[left]]<d1[s[left]]:
                    have-=1
                left+=1
                
               
            #print(ansl,ansr,anslen)
                
        return s[ansl:ansr+1] if ansl!=-1 else ""



        