class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

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
    n, m, k = list(map(int, input().split()))
    dsu = DSU(n + 1)

    for _ in range(m):
        u, v = list(map(int, input().split()))
    
    queries = []
    for _ in range(k):
        data = input().strip()
        opr, u, v = data.split(" ")
        u, v = int(u), int(v)
        queries.append((opr, u, v))
    
    queries.reverse()
    
    ans = []
    for opr, u, v in queries:
        if opr == "cut":
            dsu.union(u, v)
        else:
            ans.append(dsu.connected(u, v))
        
    for res in ans[::-1]:
        print("YES" if res else "NO")    

solve()