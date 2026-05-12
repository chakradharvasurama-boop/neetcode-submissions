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
            if course in visited:
                return False
            if course in cycleChecked:
                return True
            
            visited.add(course)
    
            for nextCourse in adj[course]:
               
         
                if not noCycle(nextCourse):
                    return False
            visited.remove(course)
            cycleChecked.add(course)

            return True

        for course in range(numCourses):
        
            
            if not noCycle(course):
                return False
            #print(ans,course)

        
        return True

        


        

        


        