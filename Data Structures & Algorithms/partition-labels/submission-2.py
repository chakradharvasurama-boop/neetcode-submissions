class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        hmap={}
        for i,c in enumerate(s):
            hmap[c]=i


        ans=[]
        start=0
        end=0
        for i,c in enumerate(s):
            end=max(end,hmap[c])
            if i==end:
                ans.append(end-start+1)
                start,end=i+1,i+1
        return ans
        '''
        n=len(s)
        hmap={}
        for c in s:
            hmap[c]=hmap.get(c,0)+1
        zeros=0
        unique=set()
        ans=[]
        start=0
        for i,c in enumerate(s):
            hmap[c]-=1
            unique.add(c)
            if hmap[c]==0:
                zeros+=1
            if len(unique)==zeros:
                ans.append(i-start+1)
                start=i+1
        return ans
        '''

        