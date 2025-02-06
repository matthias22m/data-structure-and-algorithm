# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        st = Counter(words[0])
        ans = []
        for char in st:
            for word in words:
                f = st[char]

                cnt = word.count(char)
                st[char] = min(f,cnt)
        
        for char, f in st.items():
            if f>0:
                for i in range(f):
                    ans.append(char)
        return ans

        
