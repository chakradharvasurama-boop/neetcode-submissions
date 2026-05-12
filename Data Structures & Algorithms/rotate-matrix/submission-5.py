class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)

        for i in range(n//2):
            l,r=i,n-i-1

            for j in range(r-l):
        

                topLeft=matrix[l][l+j]
                matrix[l][l+j]=matrix[r-j][l]
                matrix[r-j][l]=matrix[r][r-j]
                matrix[r][r-j]=matrix[l+j][r]
                matrix[l+j][r]=topLeft
                
                


           

       
        