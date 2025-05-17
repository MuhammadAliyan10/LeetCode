class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0] * n for _ in range(n)]
        num = 1
        top, bottom = 0, n - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                result[top][j] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1):
                result[i][right] = num
                num += 1
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result[bottom][j] = num
                    num += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result[i][left] = num
                    num += 1
                left += 1

        return result


# Test case
S = Solution()
print(S.generateMatrix(3))
