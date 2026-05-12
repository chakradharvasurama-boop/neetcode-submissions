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

    
        

        

    def search(self, word: str) -> bool:
        def recursiveSearch(node:TrieNode,i:int)->bool:
            curr=node
       
            while i<len(word):
                #print(curr)
                c=word[i]
                if c=='.':
                    ans=False
                    for child in curr.children:
                        ans|=recursiveSearch(curr.children[child],i+1)
                    return ans


                else:
                    if c not in curr.children:
                        return False
                curr=curr.children[c]
                i+=1
            return curr.word
        return recursiveSearch(self.root,0)
        
        
        
