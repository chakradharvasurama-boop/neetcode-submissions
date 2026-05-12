class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False
        self.index=-1

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
   
    


        

    def insert(self, word: str,i:int) -> None:
        curr=self.root

        
     
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.index=i
        curr.word=True


        



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        p=PrefixTree()
        m=len(board)
        n=len(board[0])
        s=set()

        for i,word in enumerate(words):
            p.insert(word,i)

        visited=[[0]*n for i in range(m)]
        ans=[]
        def backtrack(i:int,j:int,node:TrieNode):

            #print("here")
            visited[i][j]=1
            #print(node.word)
            
            if node.word:
                s.add(node.index)
          
            if i+1<m and not visited[i+1][j] and board[i+1][j] in node.children:
     
                backtrack(i+1,j,node.children[board[i+1][j]])
            if j+1<n and not visited[i][j+1]and board[i][j+1] in node.children:
           
                backtrack(i,j+1,node.children[board[i][j+1]])
            if i-1>=0 and not visited[i-1][j] and board[i-1][j] in node.children:
              
                backtrack(i-1,j,node.children[board[i-1][j]])
            if j-1>=0 and not visited[i][j-1]and board[i][j-1] in node.children:
              
                backtrack(i,j-1,node.children[board[i][j-1]])
            
      
            visited[i][j]=0
        for i in range(m):
            for j in range(n):
                if board[i][j] in p.root.children:
                    backtrack(i,j,p.root.children[board[i][j]])

        for i,word in enumerate(words):
            if i in s:
                ans.append(word)
        return ans


        
        




















        