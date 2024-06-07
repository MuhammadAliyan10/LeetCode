class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        outerPointer  = 0
        for innerPointer in range(1,len(nums)):
            if nums[outerPointer] != nums[innerPointer]:
                outerPointer += 1
                nums[outerPointer] = nums[innerPointer]
             

        return outerPointer + 1



#! Time complexity is O(n)
#! Space complexity is O(1)