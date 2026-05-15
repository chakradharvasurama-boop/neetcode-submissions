class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numberWordMap={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
       
        temp=[]
        res=[]
        if len(digits)==0:
            return []

        def backtrack(i:int):
            if i==len(digits):
                res.append(''.join(temp))
                return
            letters=numberWordMap[digits[i]]
            
            for letter in letters:
                temp.append(letter)
                backtrack(i+1)
                temp.pop()
        
        backtrack(0)
        return res 
 



        