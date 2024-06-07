class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price - minPrice > maxProfit:
                maxProfit = price - minPrice

        return maxProfit



#!Time complexity is O(n)
#! Space complexity is O(1)