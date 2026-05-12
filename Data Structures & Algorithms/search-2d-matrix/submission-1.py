class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        
        while l<=r:
            m=l+(r-l)//2
            if matrix[m][0]>target:
                r=m-1
                
            elif matrix[m][-1]<target:
             
                l=m+1
            else: 
                break
            #print(m)
        if not (l<=r):
            return False
        currm=l+(r-l)//2
        l,r=0,len(matrix[currm])-1
        while l<=r:
            m2=l+(r-l)//2
            if matrix[currm][m2]<target:
                l=m2+1
            elif matrix[currm][m2]>target:
                r=m2-1
            else:
                return True

        return False
