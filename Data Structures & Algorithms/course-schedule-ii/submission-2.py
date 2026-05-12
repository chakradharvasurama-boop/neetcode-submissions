class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre={}
        for i in range(numCourses):
            pre[i]=set()
        for i,j in prerequisites:

            pre[j].add(i)

       
        visited=set()
        order=[]
        inOrder=set()
    
        def noCycle(course: int)-> bool:
            if course in visited:
                return False
            if course in inOrder:
           
                return True
            
            visited.add(course)
    
            for preReq in pre[course]:
               
         
                if not noCycle(preReq):
                    return False
            visited.remove(course)
            pre[course]=set()
      
            order.append(course)
            inOrder.add(course)

            return True
        
        for course in range(numCourses):
            if not noCycle(course):
                #print("here")
                return []
        #print(order)
        order.reverse()
        return order 



        