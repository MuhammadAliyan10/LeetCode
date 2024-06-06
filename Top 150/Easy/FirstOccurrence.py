class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for i in range(len(haystack)):
            print(haystack[i:i+length])
            if haystack[i:i+length] == needle:
                return i
        return -1



#! Time complexity is O(n)
#! Space complexity is O(1)

