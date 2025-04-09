# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        visited = set()
        ans = False

        def dfs(vertex, visited):
            nonlocal ans
            if vertex == destination:
                ans = True
                return
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    dfs(neighbour,visited)
        dfs(source,visited)
        return ans