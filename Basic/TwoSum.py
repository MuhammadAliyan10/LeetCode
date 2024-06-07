class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numToIndex = {}
        for i, num in enumerate(nums):
           compliment = target - num
           if compliment in numToIndex:
               return [numToIndex[compliment], i]
           numToIndex[num] = i



#! Time complexity is O(n).
#! Space complexity is O(n).
#* If we use nested loops, time complexity will be O(n ^ 2)