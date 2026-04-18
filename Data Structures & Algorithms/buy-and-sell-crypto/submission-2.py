class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            if prices[i] - minimum > profit: 
                profit = prices[i] - minimum
        return profit