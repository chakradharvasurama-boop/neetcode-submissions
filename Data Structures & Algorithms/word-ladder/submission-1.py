class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj=defaultdict(list)
        n=len(wordList)
        temp=list(beginWord)
   
        
        for i in range(n):
            temp=list(wordList[i])
            for j in range(len(temp)):
                c=temp[j]
                temp[j]='*'
                adj[''.join(temp)].append(wordList[i])
                temp[j]=c
 
        q=deque()
        q.append(beginWord)
        visited=set()
        sequence=1
        visited.add(beginWord)
        while q:
            l=len(q)

            for i in range(l):
                word=q.popleft()
                

                
                temp=list(word)
                for j in range(len(temp)):
                    c=temp[j]
                    temp[j]='*'
                    patern=''.join(temp)
                    for k in range(len(adj[patern])):
                        if adj[patern][k]==endWord:
                            return sequence+1
                        if adj[patern][k] not in visited:
                            visited.add(adj[patern][k])
                            q.append(adj[patern][k])
                    temp[j]=c


            sequence+=1
        return 0

        '''
        adj=defaultdict(list)
        n=len(wordList)
        def checkDiffCount(word1,word2)->int:
            count=0
            for i in range(len(word1)):
                if word1[i]!=word2[i]:
                    count+=1
            return count
        

        for i in range(n):
            if checkDiffCount(wordList[i],beginWord)==1:
                adj[wordList[i]].append(beginWord)
                adj[beginWord].append(wordList[i])
            for j in range(i+1,n):
                if checkDiffCount(wordList[i],wordList[j])==1:
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        if endWord not in adj:
            return 0
        q=deque()
        q.append(beginWord)
        visited=set()
        sequence=1
        visited.add(beginWord)
        while q:
            l=len(q)

            for i in range(l):
                word=q.popleft()
                
                for neighbour in adj[word]:
                    if neighbour==endWord:
                        return sequence+1
                    if neighbour not in visited:
                        q.append(neighbour)
                        visited.add(neighbour)
            sequence+=1
        return 0
        '''














        






        