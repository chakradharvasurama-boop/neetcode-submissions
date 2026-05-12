class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        s=[0,0]
        e=[m-1,n-1]
        res=[]
        while s[0]<e[0] and s[1]<e[1] :
            print(s)
            pointer=s.copy()
            #travel Right
       
            while pointer[1]<e[1]:
                res.append(matrix[pointer[0]][pointer[1]])
                pointer[1]+=1
      
            #travel down
            while pointer[0]<e[0]:
                res.append(matrix[pointer[0]][pointer[1]])
                pointer[0]+=1
     
            #travel left
            while pointer[1]>s[1]:
                res.append(matrix[pointer[0]][pointer[1]])
                pointer[1]-=1
        
            while pointer[0]>s[0]:
                res.append(matrix[pointer[0]][pointer[1]])
                pointer[0]-=1
            s[0]+=1
            s[1]+=1
            e[0]-=1
            e[1]-=1
        if s[0]==e[0]:
            while s[1]<=e[1]:
                res.append(matrix[s[0]][s[1]])
                s[1]+=1
        elif s[1]==e[1]:
            while s[0]<=e[0]:
                res.append(matrix[s[0]][s[1]])
                s[0]+=1
        return res
       
          

                


            
        