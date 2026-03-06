t = int(input())

for _ in range(t):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))

    max_red = 0
    max_blue = 0

    total = 0
    for num in red:
        total += num
        max_red = max(max_red, total)

    total = 0
    for num in blue:
        total += num
        max_blue = max(max_blue, total)

    print(max_red + max_blue if max_red + max_blue >= 0 else 0)