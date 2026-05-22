class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        
        return x

    def union(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)

        if par_x == par_y:
            return
        
        if self.rank[par_x] < self.rank[par_y]:
            self.parent[par_x] = par_y
        elif self.rank[par_x] > self.rank[par_y]:
            self.parent[par_y] = par_x
        else:
            self.parent[par_x] = par_y
            self.rank[par_y] += 1
        

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
def solve():
    n, m = list(map(int, input().split()))
    dsu = UnionFind(n + 1)
    edges = []
    
    for _ in range(m):
        u, v, w = list(map(int, input().split()))
        edges.append((u, v, w))

    edges.sort(key=lambda x: x[2])
    ans = 0
    count = 0

    for u, v, w in edges:
        if dsu.connected(u, v):
            continue
        
        dsu.union(u, v)
        ans += w
        count += 1
        if count == n - 1:
            break
    
    print(ans)
    return

solve()