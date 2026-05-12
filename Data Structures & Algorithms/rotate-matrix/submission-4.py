class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        def swap(i,j,i1,j1):
            matrix[i][j],matrix[i1][j1]=matrix[i1][j1],matrix[i][j]
        n=len(matrix)
        for i in range(n//2):
            l,r=i,n-i-1
            si,sj=i,i
            ei,ej=n-i-1,n-i-1
      
  
            while l<n-i-1:
                print((i,l),(l,i))
                swap(i,l,l,n-i-1)
              
                swap(i,l,n-i-1,r)
                
                swap(i,l,r,i)
                l+=1
                r-=1

           

       
        