class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n=len(nums)
        ans=[]
        visited=[0]*n
        curr=[]
        nums.sort()
        hmap={}
        for num in nums:
            if num in hmap:
                hmap[num]+=1
            else:
                hmap[num]=1
        def backtrack(idx:int):

          
            if idx==n:
           
                ans.append(curr.copy())
                return
           
            for num in hmap:
                if hmap[num]>0:
                    hmap[num]-=1
                    curr.append(num)
                    backtrack(idx+1)
                    curr.pop()
                    hmap[num]+=1

            

        backtrack(0)
        
        return ans