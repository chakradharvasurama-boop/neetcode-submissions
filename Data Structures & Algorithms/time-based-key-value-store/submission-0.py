class TimeMap:

    def __init__(self):
        self.s={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
            if key in self.s:
                self.s[key].append((timestamp,value))
            else:
                self.s[key]=[(timestamp,value)]
            print(self.s)
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.s:
            l,r=0,len(self.s[key])-1
            nearestOrEqual=-1
            while l<=r:
                m=l+(r-l)//2
                if self.s[key][m][0]>timestamp:
                    r=m-1
                else:
                    l=m+1
                    nearestOrEqual=m


            if nearestOrEqual!=-1:
                return self.s[key][nearestOrEqual][1]
     
        return ""
        
