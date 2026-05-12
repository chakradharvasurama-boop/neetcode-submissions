class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        h,w=len(matrix),len(matrix[0])
        l,r=0,h*w

        while l<r:
            m=l+(r-l)//2
            row,col=m//w,m%w
            if matrix[row][col]<target:
                l=m+1
            elif matrix[row][col]==target:
                return True
            else:
                r=m
        return False
            


            


        
            
        