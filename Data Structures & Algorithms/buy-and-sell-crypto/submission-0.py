class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmin=prices[0]
        ans=0
        for i in range(1,len(prices)):
            if(prices[i]>currmin):
                ans=max(ans,prices[i]-currmin)
            currmin=min(prices[i],currmin)
        return ans
        