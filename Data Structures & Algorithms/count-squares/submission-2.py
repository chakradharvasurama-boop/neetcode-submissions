class CountSquares:

    def __init__(self):
        self.points={}
        

    def add(self, point: List[int]) -> None:
        t=tuple(point)
        if t in self.points:
            self.points[t]+=1
        else:
            self.points[t]=1
        

    def count(self, point: List[int]) -> int:
        count=0
        #print(self.points)
        for key in self.points:
            #print(point,key)
            xd=(point[0]-key[0])**2
            yd=(point[1]-key[1])**2
            if xd==yd and xd+yd!=0:
                if (key[0],point[1]) in self.points and (point[0],key[1]) in self.points:
                    currCount=1
                    currCount*=self.points[(key[0],point[1])]
                    currCount*=self.points[(point[0],key[1])]
                    currCount*=self.points[(key[0],key[1])]
                    count+=currCount
        return count
                    



