class MedianFinder:

    def __init__(self):
        self.arr=[]
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        curr=len(self.arr)-1
        while curr and self.arr[curr]<self.arr[curr-1]:
            self.arr[curr],self.arr[curr-1]=self.arr[curr-1],self.arr[curr]
            curr-=1

        

    def findMedian(self) -> float:
        

        if len(self.arr)%2==0:
            return (self.arr[len(self.arr)//2] +self.arr[len(self.arr)//2-1])/2
        else:
            return self.arr[len(self.arr)//2]
        
        