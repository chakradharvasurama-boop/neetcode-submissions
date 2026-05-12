class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
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
            

            visited.add(node)

            for i in adj[node]:
                if i is not prev and not dfs(node,i):
                    return False
          
            
            return True
                    

        ans=dfs(-1,0)


        return ans if len(visited)==n else False

        