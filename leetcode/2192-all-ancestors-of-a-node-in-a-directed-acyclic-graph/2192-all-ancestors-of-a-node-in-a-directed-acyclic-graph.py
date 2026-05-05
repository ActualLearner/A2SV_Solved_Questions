class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        indegree = [0] * n
        answer = [set() for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        q = deque([i for i in range(n) if indegree[i] == 0])
        while q:
            curr = q.popleft()
            for nei in adj[curr]:
                answer[nei].add(curr)
                answer[nei].update(answer[curr])

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
            
        ans = [sorted(nums) for nums in answer]
        return ans