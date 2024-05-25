class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        originalNumber = x
        reverseNumber = 0
        while x != 0:
            digit = x % 10
            reverseNumber = reverseNumber * 10 + digit
            x //= 10

        if reverseNumber < -2**31 or reverseNumber > 2**31 - 1:
            return 0
        
        return originalNumber == reverseNumber


#! Time complexity is O(log ^ 10(n))
#! Space complexity is O(!) constant.