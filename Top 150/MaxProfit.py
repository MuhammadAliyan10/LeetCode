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

s = Solution()
print(s.maxProfit([7,6,4,3,1]))