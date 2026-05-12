class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={}
        for i in range(numCourses):
            adj[i]=set()
        for i,j in prerequisites:

            adj[i].add(j)

        ans=True
        cycleChecked=set()
        visited=set()
        print()
        def noCycle(course: int)-> bool:
            if course in cycleChecked:
                return True
            
            visited.add(course)
            ans=True
            for nextCourse in adj[course]:
                if nextCourse in visited:
                    ans=False 
                    break
                
                ans&=noCycle(nextCourse)
            visited.remove(course)
            cycleChecked.add(course)

            return ans

        for course in range(numCourses):
            visited.clear()
            
            ans &=noCycle(course)
            #print(ans,course)

        
        return ans

        


        

        


        