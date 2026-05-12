class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf=0
        currbuy=prices[0]
        for i in range(1,len(prices)):
            
            if prices[i]<currbuy:
                currbuy=prices[i]
            maxProf=max(maxProf,prices[i]-currbuy)

        

        return maxProf
        