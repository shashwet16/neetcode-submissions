class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = prices[0]
        m_profit = 0
        for num in prices: 
            if num < min_prices:
                min_prices = num
            profit = num - min_prices

            if profit > m_profit: 
                m_profit = profit
        return m_profit
        