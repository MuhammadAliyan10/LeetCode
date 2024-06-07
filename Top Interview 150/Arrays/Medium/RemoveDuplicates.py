class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i : int =0
        for num in nums:
            if i < 2 or num > nums[i -2]:
                nums[i] = num
                i += 1
        return i
        



#! Time complexity is O(n)
#! Space complexity is O(1)