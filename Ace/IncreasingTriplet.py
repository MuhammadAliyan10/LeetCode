class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first: 
                first = n
            elif n <= second: 
                second = n
            else:  
                return True
        
        return False



s = Solution()
print(s.increasingTriplet([1,2,3,4,5]))