class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        def swap(i,j,i1,j1):
            matrix[i][j],matrix[i1][j1]=matrix[i1][j1],matrix[i][j]
        n=len(matrix)
        for i in range(n//2):
            si,sj=i,i
            ei,ej=n-i-1,n-i-1
            a=[si,sj]
            b=[si,ej]
            c=[ei,ej]
            d=[ei,sj]
  
            while a[1]!=ej:
                swap(a[0],a[1],b[0],b[1])
              
                swap(a[0],a[1],c[0],c[1])
                
                swap(a[0],a[1],d[0],d[1])

                a[1]+=1
                b[0]+=1
                c[1]-=1
                d[0]-=1

       
        