class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmtarget=defaultdict(int)
        hmstring=defaultdict(int)
        matches=0
        count=len(t)
        for c in t:
            hmtarget[c]+=1
            
        
        start=-1
        ansl,ansr=-1,-1
        for i,c in enumerate(s):
            if c in hmtarget:
                if start==-1:
                    start=i
                hmstring[c]+=1
                if hmstring[c]<=hmtarget[c]:
                    matches+=1
               
                    #print(i,"here")

                while s[start] not in hmtarget or  hmstring[s[start]]>hmtarget[s[start]]:
        
                    if s[start] in hmtarget:
                        hmstring[s[start]]-=1

                    start+=1
                       
                        
                if matches==count :
                    if ansl==-1 or i-start<ansr-ansl:
                        ansl=start
                        ansr=i
                
                        

            
        print(ansl,ansr)
        if ansl!=-1:
            return s[ansl:ansr+1]

        return ''

        