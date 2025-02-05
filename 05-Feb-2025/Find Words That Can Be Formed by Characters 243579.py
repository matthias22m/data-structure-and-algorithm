# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        _len = 0
        for word in words:
            copy = count.copy()
            for char in word:
                if copy[char] == 0:
                    break
                copy[char]-=1
            else:
                _len+=len(word)
        return _len