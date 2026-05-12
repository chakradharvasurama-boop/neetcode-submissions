class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums=sorted(nums)
        ans=[]
        for i in range(len(snums)):
            l,r=i+1,len(snums)-1
            if i!=0 and snums[i]==snums[i-1]:
                continue
            while(l<r):
                if l!=i+1 and snums[l]==snums[l-1]:
                    l+=1
                    continue
                if snums[l]+snums[r]>-1*snums[i]:
                    r-=1
                elif snums[l]+snums[r]<-1*snums[i]:
                    l+=1
                else:
          
                    ans.append([snums[i],snums[l],snums[r]])
                    l+=1
                    r-=1
        return ans

        