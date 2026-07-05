def solve():
    s1 = input().strip()
    s2 = input().strip()
    N = len(s1)
    final_pos = 0
    paths = 2 ** s2.count("?")

    for char in s1:
        if char == "+":
            final_pos += 1
        else:
            final_pos -= 1

    def explore(i, curr):
        if i == N:
            return 1 if curr == final_pos else 0

        if s2[i] == "?":
            return explore(i + 1, curr + 1) + explore(i + 1, curr - 1)
        elif s2[i] == "+":
            return explore(i + 1, curr + 1)
        else:
            return explore(i + 1, curr - 1)

    print(explore(0, 0) / paths)

solve()