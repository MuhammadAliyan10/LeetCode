class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        writePointer: int = 0

        for readPointer in range(len(nums)):
            if nums[readPointer] != val:
                nums[writePointer] = nums[readPointer]
                writePointer += 1

        return writePointer
    

#! Time complexity is O(n).
#! Space complexity is O(1).


