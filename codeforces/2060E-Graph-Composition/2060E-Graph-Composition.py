class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x, y):
        par_x, par_y = self.find(x), self.find(y)
        if par_x == par_y:
            return
        elif self.size[par_y] < self.size[par_x]:
            par_x, par_y = par_y, par_x

        self.parent[par_x] = par_y
        self.size[par_y] += self.size[par_x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    
t = int(input())
for _ in range(t):
    n, m1, m2 = list(map(int, input().split()))
    dsu_f = DSU(n + 1)
    dsu_g = DSU(n + 1)
    f_edges = []
    g_edges = []

    for _ in range(m1):
        u, v = list(map(int, input().split()))
        f_edges.append((u, v))
        
    for _ in range(m2):
        u, v = list(map(int, input().split()))
        g_edges.append((u, v))
        dsu_g.union(u, v)
    
    ans = 0
    for u, v in f_edges:
        if not dsu_g.connected(u, v):
            ans += 1
            continue

        dsu_f.union(u, v)

    for u, v in g_edges:
        if dsu_f.connected(u, v):
            continue

        ans += 1
        dsu_f.union(u, v)

    print(ans)