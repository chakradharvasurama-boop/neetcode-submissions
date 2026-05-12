class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        maskRows=(1<<m)-1
        maskCols=(1<<n)-1
        firstRowZero=False
        firstColZero=False
       
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    if i==0 and j==0:
                        firstRowZero=True
                        firstColZero=True
                    elif i==0 and j!=0:
                        firstRowZero=True

                    elif j==0 and i!=0:
                        firstColZero=True
                    else:
                        matrix[i][0]=0
                        matrix[0][j]=0

        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(n):
                    matrix[i][j]=0
        for j in range(1,n):
            if matrix[0][j]==0:
                for i in range(m):
                    matrix[i][j]=0
        if firstRowZero:
            for j in range(0,n):
                matrix[0][j]=0
        if firstColZero:
            for i in range(0,m):
                matrix[i][0]=0

                    

       


        #[1,0,3,6]
        #[4,0,5,7]
        #[6,7,8,8]
        #[6,7,8,8]

        
                    
        
        