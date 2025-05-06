class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


S = Solution()
print(S.containsDuplicate([1, 2, 3, 4, 5]))
