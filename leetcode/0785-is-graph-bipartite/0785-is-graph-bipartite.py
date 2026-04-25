class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        color = False

        def divide(node, color):
            visited[node] = color

            for nei in graph[node]:
                if nei in visited and visited[nei] == color:
                    return False
                elif nei not in visited:
                    if not divide(nei, not color):
                        return False
                
            return True
        
        for i in range(len(graph)):
            if i not in visited and not divide(i, color):
                return False
        
        return True