# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(set)
        balls = {}
        ans = []
        for ball,color in queries:
            if ball in balls:
                colors[balls[ball]].remove(ball)
                if not colors[balls[ball]]:
                    del colors[balls[ball]]

            colors[color].add(ball)
            balls[ball] = color
            ans.append(len(colors))
        return ans