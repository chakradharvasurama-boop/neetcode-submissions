class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
        sortedList=sorted([(key,value) for key,value in d.items()],key=lambda x: x[1],reverse=True)

        return [x[0] for x in sortedList[0:k]]
        