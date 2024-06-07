class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        n = len(nums)
        k = k % n
        def reverse(nums: list[int], start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(nums, 0, n - 1)

        reverse(nums, 0, k - 1)

        reverse(nums, k, n - 1)



#! Time complexity is O(n)
#! Space complexity is O(1)