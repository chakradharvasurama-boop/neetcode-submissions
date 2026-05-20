class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre={}
        for i in range(numCourses):
            pre[i]=set()
        for i,j in prerequisites:

            pre[j].add(i)

       
        visited=set()
        path=set()
    
        def noCycle(course: int)-> bool:
            if course in path:
                return False
            if len(pre[course])==0 or course in visited:
                return True
            
            visited.add(course)
            path.add(course)
    
            for preReq in pre[course]:
               
         
                if not noCycle(preReq):
                    return False
            path.remove(course)
            

            return True

        for course in range(numCourses):
        
            
            if not noCycle(course):
                return False
            #print(ans,course)

        
        return True

        


        

        


        