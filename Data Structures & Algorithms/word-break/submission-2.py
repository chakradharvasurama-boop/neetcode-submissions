
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


    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return curr.word


    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr=curr.children[c]
        return True
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

        


        def backtrack(i:int)->bool:
            if i in dp:
                return dp[i]

            end=min(i+maxDictWordLen,n)
            dp[i]=False

            for j in range(i,end):
                if wordSTrie.search(s[i:j+1]):
                    dp[i]|=backtrack(j+1)
            return dp[i]
        
           
        return backtrack(0)





        