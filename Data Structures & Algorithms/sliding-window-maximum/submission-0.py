from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #[1,2,1,0,4,2,6]
        #10 9 8 7 6 5
        s=SortedList()
        ans=[]
        for i in range(k):
            s.add(nums[i])
        ans.append(s[-1])
        left=0
        for i in range(k,len(nums)):
            s.remove(nums[left])
            
            left+=1
            s.add(nums[i])
            #print(left,i,s[-1])
            ans.append(s[-1])
        return ans


        