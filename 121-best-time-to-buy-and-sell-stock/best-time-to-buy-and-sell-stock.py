class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = 0
        m = float('inf')
        for i in range(len(prices)-1):
            if m > prices[i]:
                m = prices[i]
                p = max(prices[i+1:])
                d = max(p-m,d)
        
        return d
        