class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans=[]
        def generate(op,cl,s,size,ans):
            if(op<size):
                generate(op+1,cl,s+'(',size,ans)
            if(cl<op):
                generate(op,cl+1,s+')',size,ans)
            if(op==size and cl==size):
                ans.append(s)
        generate(0,0,"",n,ans)
        return ans





        