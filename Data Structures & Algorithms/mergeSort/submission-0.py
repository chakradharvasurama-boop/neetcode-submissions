# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(l:int,m:int,r:int):
        #print(l,m,r)
            l1=pairs[l:m+1]
            l2=pairs[m+1:r+1]
            n1,n2=len(l1),len(l2)
            p1,p2=0,0
            curr=l
            while p1<n1 and p2<n2:
                if l1[p1].key<=l2[p2].key:
                    pairs[curr]=l1[p1]
                    p1+=1
                else:
                    pairs[curr]=l2[p2]
                    p2+=1
                curr+=1
            while p1<n1:
                pairs[curr]=l1[p1]
                p1+=1
                curr+=1
            while p2<n2:
                pairs[curr]=l2[p2]
                p2+=1
                curr+=1
            
            
    
    
        def merge_sort(l:int,r:int):
            if l>=r:
                return
            m=l+(r-l)//2
            
            merge_sort(l,m)
            merge_sort(m+1,r)
            merge(l,m,r)
        merge_sort(0,len(pairs)-1)
        return pairs

