class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        sorted_list = sorted(nums)
        for i, v in enumerate(sorted_list):
            if i != v:
                return v - 1
            if v == len(nums) - 1:
                return v + 1


S = Solution()
print(S.missingNumber([0, 1]))
