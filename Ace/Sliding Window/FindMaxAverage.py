class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        currentSum = sum(nums[:k])
        maxSum = currentSum
        for i in range(k, len(nums)):
            currentSum = currentSum - nums[i - k] + nums[i]
            maxSum = max(maxSum, currentSum)
        return maxSum / k


s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))