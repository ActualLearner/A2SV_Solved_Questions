import sys
input = sys.stdin.readline
results = []

h, w = list(map(int, input().split()))
matrix = [" " * (w + 1)]
for _ in range(h):
    matrix.append(" " + input().strip())

hz = [[0] * (w + 1) for _ in range(h + 1)]
vt = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        val_hz, val_vt = 0, 0

        if matrix[i][j] == "." and matrix[i][j - 1] == ".":
            val_hz = 1
        if matrix[i][j] == "." and matrix[i - 1][j] == ".":
            val_vt = 1    

        hz[i][j] = val_hz + hz[i - 1][j] + hz[i][j - 1] - hz[i - 1][j - 1]
        vt[i][j] = val_vt + vt[i - 1][j] + vt[i][j - 1] - vt[i - 1][j - 1]

def get_sum(pref, r1, c1, r2, c2):
    if r1 > r2 or c1 > c2: return 0
    return pref[r2][c2] - pref[r1-1][c2] - pref[r2][c1-1] + pref[r1-1][c1-1]

q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = list(map(int, input().split()))
    ans = get_sum(hz, r1, c1 + 1, r2, c2) + get_sum(vt, r1 + 1, c1, r2, c2)
    results.append(str(ans))

sys.stdout.write("\n".join(results))