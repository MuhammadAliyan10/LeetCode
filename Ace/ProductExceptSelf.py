class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]
        
        rightProduct = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= rightProduct
            rightProduct *= nums[i]
        
        return answer

s = Solution()
print(s.productExceptSelf([1,2,3,4]))