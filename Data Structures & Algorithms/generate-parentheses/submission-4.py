class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp=[]
        ans=[]
    
        
        def backtrack(openUsed,closeUsed)->None:
            if closeUsed==n:
                
                ans.append(''.join(temp))

                return 
            #print(temp)
       
        
            #add open para
            if openUsed<n:
                temp.append('(')
                backtrack(openUsed+1,closeUsed)
                temp.pop()
            #add closed para
            if closeUsed<openUsed:
                temp.append(')')
                backtrack(openUsed,closeUsed+1)
                temp.pop()
    
        backtrack(0,0)
        return ans
        
            
            

        