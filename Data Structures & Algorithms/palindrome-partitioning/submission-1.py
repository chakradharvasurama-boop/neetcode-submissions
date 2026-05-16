class Solution:
    def partition(self, s: str) -> List[List[str]]:

        curr=[]
        ans=[]
        n=len(s)
        def isPalindrome(k)->bool:
            i=0
            j=len(curr[k])-1
            while i<j:
                if curr[k][i]!=curr[k][j]:
                    return False
                i+=1
                j-=1
            return True

        def backtrack(i:int):
            if i==n:
                ans.append([''.join(st) for st in curr])
                return

            curr.append([s[i]]) 
            backtrack(i+1)  

            for j in range(i+1,n):

                curr[-1].append(s[j])
                if isPalindrome(len(curr)-1):
                    backtrack(j+1)
                
            curr.pop()

        backtrack(0)
        return ans
        