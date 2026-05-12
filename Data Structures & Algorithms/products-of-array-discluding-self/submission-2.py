class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p=[]
        ans=[]
        temp=1

        for i in range(n-1,-1,-1):
            p.append(nums[i]*temp)
            temp*=nums[i]
        temp=1
        p.reverse()
        for i in range(n):
            t=temp*nums[i]
            if i!=n-1:
                ans.append(temp*p[i+1])
            else:
                ans.append(temp)
            temp=t
        return ans
            


            
        