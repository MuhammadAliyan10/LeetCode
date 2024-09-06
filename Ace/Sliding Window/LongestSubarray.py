class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zeroCount = 0
        maxLength = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            maxLength = max(maxLength, right - left)
        return maxLength




s = Solution()
nums = [1,1,0,1]
print(s.longestSubarray(nums))