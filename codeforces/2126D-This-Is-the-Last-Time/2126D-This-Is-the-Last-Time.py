import sys
data = list(map(int, sys.stdin.read().split()))
t = data[0]
idx = 1
ans = []

for _ in range(t):
    n = data[idx]
    m = n*3
    k = data[idx+1]
    idx += 2
    casinos = []

    for i in range(idx, idx+m, 3):
        casinos.append((data[i], data[i+1], data[i+2]))
    idx += m

    casinos.sort()
    start = k

    for c in casinos:
        if c[0] <= start and start <= c[1] and start <= c[2]:
            start = c[2]

    ans.append(str(start))

sys.stdout.write("\n".join(ans))