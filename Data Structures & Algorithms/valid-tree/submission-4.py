class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==1 and edges==[]:
            return True
        adj={}
        for i in range(n):
            adj[i]=[]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
            

        visited=set()

        def dfs(prev: int,node: int) -> bool:
            if node in visited:
                return False
            if adj[node]==[]:
                return False

            visited.add(node)

            for i in adj[node]:
                if i is not prev and not dfs(node,i):
                    return False
          
            
            return True
                    

        ans=dfs(-1,0)


        return ans if len(visited)==n else False

        