class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        
        def dfs(node, path):
            nonlocal n
            path.append(node)
            if node == n - 1:
                ans.append(path[:])

            for nei in graph[node]:
                dfs(nei, path)
            path.pop()
        
        dfs(0, [])
        return ans