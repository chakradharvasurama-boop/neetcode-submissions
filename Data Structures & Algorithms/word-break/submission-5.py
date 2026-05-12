
class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

        

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.word=True


class Solution:
    
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSTrie=PrefixTree()
        maxDictWordLen=0
        for word in wordDict:
            wordSTrie.insert(word)
            maxDictWordLen=max(len(word),maxDictWordLen)
        n=len(s)
        dp={}
        dp[n]=True
        for i in range(n-1,-1,-1):
            end=min(i+maxDictWordLen,n)
            dp[i]=False
            curr=wordSTrie.root
            for j in range(i,end):
                if s[j] in curr.children:
                    curr=curr.children[s[j]]
                else:
                    break
                if curr.word:
                    dp[i]|=dp[j+1]
                if dp[i]:
                    break

        return dp[0]

        '''
        wordSTrie=PrefixTree()
        maxDictWordLen=0
        for word in wordDict:
            wordSTrie.insert(word)
            maxDictWordLen=max(len(word),maxDictWordLen)
        n=len(s)
        dp={}
        dp[n]=True

        
       


        def backtrack(i:int)->bool:
            if i in dp:
                return dp[i]

            end=min(i+maxDictWordLen,n)
            dp[i]=False
            curr=wordSTrie.root
            for j in range(i,end):
                if s[j] in curr.children:
                    curr=curr.children[s[j]]
                else:
                    break
                if curr.word:
                    dp[i]|=backtrack(j+1)
                if dp[i]:
                    return True
                
            return dp[i]
        
           
        return backtrack(0)
        '''





        