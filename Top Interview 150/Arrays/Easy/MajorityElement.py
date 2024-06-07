class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)

        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) // 2:
            return candidate
        else:
             return -1

      
    


#! Time complexity is O(n).
#! Space complexity is O(1).