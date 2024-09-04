class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandy = max(candies)
        return [(candy + extraCandies) >= maxCandy for candy in candies]

            

s = Solution()
print(s.kidsWithCandies([12,1,12],10))
