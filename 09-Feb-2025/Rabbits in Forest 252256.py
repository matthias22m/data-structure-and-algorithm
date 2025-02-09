# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        _sum = 0
        count = Counter(answers)
        for num,cnt in count.items():
            _sum += (num+1)*ceil(cnt/(num+1))
        return _sum