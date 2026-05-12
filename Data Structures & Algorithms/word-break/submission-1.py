
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
        for word in wordDict:
            wordSTrie.insert(word)
        n=len(s)
        hmap={}

        


        def backtrack(i:int,curr:str)->bool:
            if i==n:

                return not curr
            if i in hmap and curr in hmap[i]:
                return  hmap[i][curr]
            elif  i in hmap:
                hmap[i][curr]=False
            else:
                hmap[i]={}
                hmap[i][curr]=False




            hmap[i][curr]=False

            if wordSTrie.search(curr+s[i]):
                hmap[i][curr]|=backtrack(i+1,"")
            

            hmap[i][curr]|=backtrack(i+1,curr+s[i])
            
           
      
            return hmap[i][curr]
        return backtrack(0,"")





        