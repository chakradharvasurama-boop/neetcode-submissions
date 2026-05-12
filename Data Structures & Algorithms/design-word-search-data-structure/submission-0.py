class TrieNode():
    def __init__(self):
        self.children={}
        self.word=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
        

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.word=True

    def recursiveSearch(self,node:TrieNode,word:str,i:int)->bool:
        curr=node
       
        while i<len(word):
            #print(curr)
            c=word[i]
            if c=='.':
                ans=False
                for child in curr.children:
                    ans|=self.recursiveSearch(curr.children[child],word,i+1)
                return ans


            else:
                if c not in curr.children:
                    return False
            curr=curr.children[c]
            i+=1
        return curr.word
        

        

    def search(self, word: str) -> bool:
        return self.recursiveSearch(self.root,word,0)
        
        
        
