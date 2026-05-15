class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp=[]
        ans=[]
    
        
        def backtrack(remainingClose)->None:
            if remainingClose==0:
                
                ans.append(''.join(temp))

                return 
            #print(temp)
            currentOpen=len(temp)-(n-remainingClose)
            currenClose=n-remainingClose
        
            #add open para
            if currentOpen<n:
                temp.append('(')
                backtrack(remainingClose)
                temp.pop()
            #add closed para
            if currenClose<currentOpen:
                temp.append(')')
                backtrack(remainingClose-1)
                temp.pop()
    
        backtrack(n)
        return ans
        
            
            

        