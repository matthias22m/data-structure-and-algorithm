# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        _sum = skill[0]+skill[-1]
        chemistry = 0
        right, left = len(skill)-1, 0
        while right > left:
            if _sum != skill[right]+skill[left]:
                return -1
            chemistry += skill[right]*skill[left]
            right-=1
            left+=1
        return chemistry