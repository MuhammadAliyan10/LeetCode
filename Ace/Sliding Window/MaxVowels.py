class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Define a set of vowels for easy lookup
        vowels = set('aeiou')
        
        # Count the number of vowels in the first window of size k
        current_vowel_count = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowel_count += 1

        max_vowel_count = current_vowel_count
        
        for i in range(k, len(s)):
        
            if s[i - k] in vowels:
                current_vowel_count -= 1

            if s[i] in vowels:
                current_vowel_count += 1

            max_vowel_count = max(max_vowel_count, current_vowel_count)
        
        return max_vowel_count

s = Solution()
print(s.maxVowels("abciiidef", 3)) 

