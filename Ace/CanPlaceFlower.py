class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        i = 0
        length = len(flowerbed)
        while i < length:
            if flowerbed[i] == 0:
                prevEmpty = (i == 0 or flowerbed[i-1] == 0)
                nextEmpty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                if prevEmpty and nextEmpty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
                    i += 1
            i += 1
        return count >= n

s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1], 1))


