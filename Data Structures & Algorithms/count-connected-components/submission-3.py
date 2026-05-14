class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        hmap={}
        for i in range(n):
            hmap[i]=[]

        for edge in edges:
            hmap[edge[0]].append(edge[1])
            hmap[edge[1]].append(edge[0])
        visited=[0]*n
        def dfs(x:int):
            visited[x]=1
            for i in hmap[x]:
                if not visited[i]:
                    dfs(i)
        ans=0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans+=1
        return ans


        


        
        

            
        