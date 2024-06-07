class Solution:
    def romanToInt(self, s: str) -> int:
     romanNumbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
     result = 0
     for i in range(len(s)):
         if i > 0 and romanNumbers[s[i]] > romanNumbers[s[i - 1]]:
             result += romanNumbers[s[i]] - 2 * romanNumbers[s[i - 1]]
         else:
             result += romanNumbers[s[i]]
     return result



#! Time complexity is O(n) 
#! Space complexity is O(1) 


