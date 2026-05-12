class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen=len(nums1)+len(nums2)
        middle=(totalLen//2)
        l1=nums1
        l2=nums2
        if len(nums1)>len(nums2):
            l1=nums2
            l2=nums1

        l=0
        r=len(l1)-1
        n1=len(l1)
        n2=len(l2)
        while l<=r:
            m=l+(r-l)//2
            
            l2Index=middle-m-1


            leftMax=max(l1[m],l2[l2Index])
            rightMin=0
            #print(leftMax,m,l2Index)
            if m+1<len(l1) and l2Index+1<len(l2):

                rightMin=min(l1[m+1],l2[l2Index+1])
            elif m+1<len(l1):
                rightMin=l1[m+1]
            elif l2Index+1<len(l2):
                rightMin=l2[l2Index+1]
            else:
           
                return (l1[m]+l2[l2Index])/2

            #print(leftMax,rightMin)

            if leftMax<=rightMin:
                if totalLen%2!=0:
                    return leftMax
                else:
                    secondMax=min(l1[m],l2[l2Index])
                    if m-1>=0:
                        secondMax=max(l1[m-1],secondMax)
                    if l2Index-1>=0:
                        secondMax=max(l2[l2Index-1],secondMax)
                    return (leftMax+secondMax)/2


            else:
                if leftMax==l1[m]:
                    r=m-1
                    
                else:
                    l=m+1
                    
        if totalLen%2!=0:
            return l2[middle]
        else:
            return (l2[middle]+l2[middle-1])/2

            






        

        

        
        