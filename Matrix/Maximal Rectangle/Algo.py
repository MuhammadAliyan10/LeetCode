class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0

        heights = heights + [0]

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]

                width = i - (stack[-1] if stack else -1) - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area


S = Solution()
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(S.maximalRectangle(matrix))
