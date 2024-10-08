class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0  
        for right in range(len(nums)):  
            if nums[right] == 0:
                k -= 1 
            
            if k < 0:  
                if nums[left] == 0:  
                    k += 1
                left += 1  #
        
        return len(nums) - left 
s = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(s.longestOnes(nums, k))  # Output will be 6
