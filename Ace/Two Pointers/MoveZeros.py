class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1



s = Solution()
s.moveZeroes([0,1,0,3,12])

        