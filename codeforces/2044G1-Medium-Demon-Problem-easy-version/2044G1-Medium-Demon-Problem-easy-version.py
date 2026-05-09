import sys
sys.setrecursionlimit(10**9)
from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    adj = [0] * n
    indeg = [0] * n

    for i in range(len(nums)):
        adj[i] = nums[i] - 1
        indeg[nums[i] - 1] += 1
    
    q = deque([i for i in range(n) if indeg[i] == 0])
    depth = [1] * n
    max_ = 0

    while q:
        curr = q.popleft()
        max_ = max(max_, depth[curr])
        nei = adj[curr]
        depth[nei] = max(depth[nei], depth[curr] + 1)
        indeg[nei] -= 1
        if indeg[nei] == 0:
            q.append(nei)
    
    print(max_ + 2)