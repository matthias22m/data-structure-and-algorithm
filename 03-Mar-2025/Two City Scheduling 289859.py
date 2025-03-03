# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost : cost[0]-cost[1])
        _sum = 0
        
        for a,b in costs[:len(costs)//2]:
            _sum+=a
        for a,b in costs[len(costs)//2:]:
            _sum+=b

        return _sum