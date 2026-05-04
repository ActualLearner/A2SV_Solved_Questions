class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = defaultdict(list)

        for i in range(n):
            x, y, r = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                a, b, c = bombs[j]
                if (x - a) ** 2 + (y - b) ** 2  <= r ** 2:
                    adj[i].append(j)
        
        def dfs(node, vis):
            vis.add(node)
            count = 1

            for nei in adj[node]:
                if nei not in vis:
                    count += dfs(nei, vis)
            
            return count
        
        ans = float("-inf")
        for i in range(n):
            ans = max(ans, dfs(i, set()))
        
        return ans