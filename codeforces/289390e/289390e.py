class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.members = [[i] for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)

        if par_x == par_y:
            return par_x
        
        if self.rank[par_x] < self.rank[par_y]:
            self.parent[par_x] = par_y
            self.members[par_y].extend(self.members[par_x])
            self.members[par_x] = []
            return par_y
        elif self.rank[par_x] > self.rank[par_y]:
            self.parent[par_y] = par_x
            self.members[par_x].extend(self.members[par_y])
            self.members[par_y] = []
            return par_x
        else:
            self.parent[par_x] = par_y
            self.rank[par_y] += 1
            self.members[par_y].extend(self.members[par_x])
            self.members[par_x] = []
            return par_y
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    


n, m = list(map(int, input().split()))
edges = []
seen = set()
monkeys = []

for _ in range(n):
    l, r = list(map(int, input().split()))
    monkeys.append((l, r))

for _ in range(m):
    edges.append(tuple(map(int, input().split())))

ans = [-1] * (n + 1)
edges_set = set(edges)
dsu = DSU(n + 1)

for i in range(n):
    l, r = monkeys[i]
    if l != -1 and (i + 1, 1) not in edges_set:
        dsu.union(i + 1, l)
    if r != -1 and (i + 1, 2) not in edges_set:
        dsu.union(i + 1, r)

for i in range(m - 1, -1, -1):
    p, h = edges[i]
    monkey_being_held = monkeys[p - 1][0] if h == 1 else monkeys[p - 1][1]

    par_p = dsu.find(p)
    par_held = dsu.find(monkey_being_held)
    root = dsu.find(1)

    if par_p == par_held:
        continue

    if par_p == root and par_held != root:
        for m in dsu.members[par_held]:
            ans[m] = i
    elif par_p != root and par_held == root:
        for m in dsu.members[par_p]:
            ans[m] = i
    
    dsu.union(par_p, par_held)

for num in ans[1:]:
    print(num)