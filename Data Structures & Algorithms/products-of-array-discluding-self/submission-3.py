class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p=[]

        temp=1

        for i in range(n-1,-1,-1):
            p.append(temp)
            temp*=nums[i]
        temp=1
        p.reverse()
        for i in range(n):
            t=temp*nums[i]
            p[i]*=temp
            temp=t
        return p
            


            
        