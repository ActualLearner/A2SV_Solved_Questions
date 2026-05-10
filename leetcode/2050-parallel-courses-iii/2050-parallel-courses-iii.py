class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        indeg = [0] * n

        for u, v in relations:
            u -= 1
            v -= 1
            adj[u].append(v)
            indeg[v] += 1
        
        q = deque([i for i in range(n) if indeg[i] == 0])
        finish = list(time)

        while q:
            curr = q.popleft()

            for nei in adj[curr]:
                finish[nei] = max(finish[nei], finish[curr] + time[nei])
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return max(finish)
