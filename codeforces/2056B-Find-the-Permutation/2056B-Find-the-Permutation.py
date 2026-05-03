t = int(input())
for _ in range(t):
    n = int(input())
    adj = [input().strip() for _ in range(n)]
    ans = [0] * n

    for i in range(len(adj)):
        before = 0
        for j in range(len(adj[0])):
            if i == j:
                continue
            elif i < j:
                if adj[i][j] == "1":
                    before += 1
            elif i > j:
                if adj[i][j] == "0":
                    before += 1

        ans[before] = i + 1

    ans.reverse()

    print(*ans)