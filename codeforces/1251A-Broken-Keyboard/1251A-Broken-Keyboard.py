t = int(input())

for _ in range(t):
    s = list(input())
    ans = set()

    if len(s) == 1:
        print(*s)
        continue

    i = 0
    counter = 0

    while i < len(s):
        if i == len(s) - 1 or s[i] != s[i + 1]:
            counter += 1
            if counter % 2 != 0:
                ans.add(s[i])
            counter = 0
            i += 1
        elif s[i] == s[i + 1]:
            i += 1
            counter += 1

    print("".join(sorted(ans)))