class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0  # Pointer for where to write in the array
        i = 0  # Pointer for reading the array

        while i < len(chars):
            char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

s = Solution()

chars1 = ["a","a","b","b","c","c","c"]
print(s.compress(chars1))  #

