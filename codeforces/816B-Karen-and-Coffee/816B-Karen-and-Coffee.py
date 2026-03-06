import sys
data = list(map(int, sys.stdin.read().split()))
n, k, q = data[0], data[1], data[2]
idx = 3

ans = []
prefix = [0] * 200_002
rec = [0] * 200_002
min_num = 0

for _ in range(n):
    l, r = data[idx], data[idx + 1]
    idx += 2

    prefix[l] += 1
    prefix[r+1] -= 1

rec[0] = prefix[0]

for i in range(1, len(prefix)):
    prefix[i] += prefix[i - 1]
    if prefix[i] >= k:
        rec[i] = (1 + rec[i - 1])
    else:
        rec[i] = rec[i - 1]

for _ in range(q):
    a, b = data[idx], data[idx + 1]
    idx += 2

    curr = rec[b] - rec[a - 1]

    if curr >= 0:
        ans.append(str(curr))

sys.stdout.write("\n".join(ans))