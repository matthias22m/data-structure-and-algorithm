# Problem: Count Vowel Substrings of a String - https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        size = len(word)
        res = 0

        for start in range(size - 4):
            for end in range(start + 5, size + 1):
                if set(word[start:end]) == vowels:
                    res += 1
        return res