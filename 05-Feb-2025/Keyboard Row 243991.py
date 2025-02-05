# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = {1:set('qwertyuiop'),2:set('asdfghjkl'),3:set('zxcvbnm')}
        ans = []

        for word in words:
            fl = True
            if word[0].lower() in keyboard[1]:
                for char in word:
                    if char.lower() not in keyboard[1]:
                        fl=False
            elif word[0].lower() in keyboard[2]:
                for char in word:
                    if char.lower() not in keyboard[2]:
                        fl=False
            elif word[0].lower() in keyboard[3]:
                for char in word:
                    if char.lower() not in keyboard[3]:
                        fl=False
            if fl:
                ans.append(word)
            else:
                fl = True
        return ans