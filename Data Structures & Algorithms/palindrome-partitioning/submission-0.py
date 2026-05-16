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
                for j in range(len(curr)):
                    if not isPalindrome(j):
                        return
                ans.append([''.join(st) for st in curr])
                return
                


            curr.append([s[i]])
            backtrack(i+1)
            curr.pop()
            if len(curr)>0:
                curr[-1].append(s[i])
                backtrack(i+1)
                curr[-1].pop()
        backtrack(0)
        return ans
        