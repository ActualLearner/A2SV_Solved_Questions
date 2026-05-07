import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)

def solve():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    idx = 1
    adj = defaultdict(list)
    start = None

    for _ in range(n - 1):
        u, v = data[idx], data[idx + 1]
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        if not start:
            start = u

    def farthest_node(start):
        dist = [-1] * (n + 1)
        q = deque([start])
        dist[start] = 0
        far_node = start

        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)

                    if dist[v] > dist[far_node]:
                        far_node = v

        return far_node, dist[far_node]

    if n == 1:
        print(0)
    else:
        temp, _ = farthest_node(start)
        _, d = farthest_node(temp)
        print(3 * d)

solve()