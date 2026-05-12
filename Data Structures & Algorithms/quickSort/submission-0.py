# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

    # Write your code here.
        def run_quick_sort(l:int,r:int):
            if l>=r:
                return
            
            pivot=r
            curr=l
            
            for i in range(l,r):
                if pairs[i].key<pairs[pivot].key:
                    pairs[i],pairs[curr]=pairs[curr],pairs[i]
                    curr+=1
            pairs[curr],pairs[pivot]=pairs[pivot],pairs[curr]
            run_quick_sort(l,curr-1)
            run_quick_sort(curr+1,r)
        
        run_quick_sort(0,len(pairs)-1)
        return pairs
        