class TimeMap:

    def __init__(self):
        self.hmap={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in  self.hmap:
            self.hmap[key]=[]
        self.hmap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        arr=self.hmap[key]

        l,r=0,len(arr)
        while l<r:
            m=l+(r-l)//2
            if arr[m][0]>timestamp:
                r=m
            elif arr[m][0]<timestamp:
                l=m+1

            else:
                return arr[m][1]
        if r-1>=0:
            return arr[r-1][1]
        return ""
        
