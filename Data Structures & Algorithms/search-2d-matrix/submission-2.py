class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)
        while l<r:
            m=l+(r-l)//2
            if matrix[m][0]<target:
                l=m+1
            elif matrix[m][0]>target:
                r=m
            else:
                return True

        row=r-1
        l,r=0,len(matrix[row])
        while l<r:
            m=l+(r-l)//2
            if matrix[row][m]>=target:
                r=m
            else:
                l=m+1

        return r<len(matrix[row]) and matrix[row][r]==target

            


        
            
        