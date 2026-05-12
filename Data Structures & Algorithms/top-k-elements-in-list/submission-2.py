class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
        m=max(d.values())
        counts=[[] for i in range(m+1)]
        for key in d:
            counts[d[key]].append(key)
        counts.reverse()
        ans=[]
        #print(counts)
        for l in counts:
            if len(l)>0:
                for num in l:
                    ans.append(num)
                    k-=1
                    if k==0:
                        return ans

        return ans
        