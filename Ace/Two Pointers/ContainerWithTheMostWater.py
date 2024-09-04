class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_height = 0  
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > max_height:
                max_height = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_height  

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7])) 
