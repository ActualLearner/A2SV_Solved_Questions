from collections import deque


def solve():

    n = int(input())
    names = [input().strip() for _ in range(n)]
    adj = {chr(i): [] for i in range(97, 123)}
    indegree = {chr(i): 0 for i in range(97, 123)}

    for i in range(n - 1):
        w1, w2 = names[i], names[i + 1]
        min_len = min(len(w1), len(w2))

        for j in range(min_len):
            if w1[j] != w2[j]:
                u = w1[j]
                v = w2[j]
                adj[u].append(v)
                indegree[v] += 1
                break
        else:
            if len(w1) > len(w2):
                print("Impossible")
                return

    queue = deque([char for char in indegree if indegree[char] == 0])
    ans = []

    while queue:
        current_char = queue.popleft()
        ans.append(current_char)

        for nei in adj[current_char]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                queue.append(nei)

    if len(ans) == 26:
        print("".join(ans))
    else:
        print("Impossible")


solve()