class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre={}
        for i in range(numCourses):
            pre[i]=set()
        for i,j in prerequisites:

            pre[j].add(i)

       
        visited=set()
    
        def noCycle(course: int)-> bool:
            if course in visited:
                return False
            if len(pre[course])==0:
                return True
            
            visited.add(course)
    
            for preReq in pre[course]:
               
         
                if not noCycle(preReq):
                    return False
            visited.remove(course)
            pre[course]=set()

            return True

        for course in range(numCourses):
        
            
            if not noCycle(course):
                return False
            #print(ans,course)

        
        return True

        


        

        


        