class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        division = defaultdict(bool)

        def dfs(node, color):
            visited.add(node)
            division[node] = color

            for nei in graph[node]:
                if nei in visited and division[nei] == color:
                    return False
                elif nei not in visited:
                    if not dfs(nei, not color):
                        return False
            
            return True
        
        for i in range(len(graph)):
            if i not in visited and not dfs(i, False):
                return False
        
        return True