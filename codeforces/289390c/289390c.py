class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.points = [0] * n
        self.size = [1] * n
    
    def find(self, i):
        if self.parent[i] == i:
            return i
          
        p = self.parent[i]
        root = self.find(p)
        
        if p != root:
            self.points[i] += self.points[p]
            
        self.parent[i] = root
        return root
    
    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        
        if irep != jrep:
            if self.size[irep] < self.size[jrep]:
                irep, jrep = jrep, irep
                
            self.parent[jrep] = irep
            self.size[irep] += self.size[jrep]
            self.points[jrep] -= self.points[irep]
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

n, m = list(map(int, input().split()))
dsu = DSU(n + 1)
for _ in range(m):
    data = input().split()
    
    if data[0] == "join":
        dsu.union(int(data[1]), int(data[2]))
        
    elif data[0] == "add":
        x = dsu.find(int(data[1]))
        dsu.points[x] += int(data[2])
        
    elif data[0] == "get":
        x = int(data[1])
        root = dsu.find(x)
        if x == root:
            print(dsu.points[x])
        else:
            print(dsu.points[x] + dsu.points[root])