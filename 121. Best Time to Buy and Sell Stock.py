class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy_price = prices[0]
        for price in prices:
            if price < buy_price:
                buy_price = price
            elif price - buy_price > ans:
                ans = price - buy_price
        return ans
