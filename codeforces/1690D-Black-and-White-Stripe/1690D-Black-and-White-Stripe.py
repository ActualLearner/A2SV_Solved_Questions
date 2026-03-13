t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    arr = list(input().strip())

    prefix = [0]

    for char in arr:
        prefix.append(prefix[-1] + (1 if char == "W" else 0))

    min_ = 10**18
    for i in range(n - k + 1):
        j = i + k
        min_ = min(min_, prefix[j] - prefix[i])

    print(min_)