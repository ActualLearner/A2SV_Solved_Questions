class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indeg = [0] * n
        ancestors = [set() for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1
        
        queue = deque([i for i in range(n) if indeg[i] == 0])
        while queue:
            curr = queue.popleft()
            for v in adj[curr]:
                ancestors[v].add(curr)
                ancestors[v].update(ancestors[curr])
                indeg[v] -= 1

                if indeg[v] == 0:
                    queue.append(v)
        
        return [sorted(nums) for nums in ancestors]