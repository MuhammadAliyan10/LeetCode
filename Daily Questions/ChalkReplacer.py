class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
       total_chalk = sum(chalk)
       k = k % total_chalk  

       for i in range(len(chalk)):
        if k < chalk[i]:  
            return i
        k -= chalk[i]
            



s = Solution()
print(s.chalkReplacer([3,4,1,2], 25))
