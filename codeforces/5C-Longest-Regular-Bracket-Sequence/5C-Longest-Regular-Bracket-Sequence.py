import sys
s = sys.stdin.read().strip()
n = len(s)

stack = [-1]
max_ = 0
ans = 0
count = 0

for i in range(n):
    if s[i] == ")":
        idx = stack.pop()
        if not stack:
            stack.append(i)
        elif i - stack[-1] > max_:
            ans = 1
            max_ = i - stack[-1]
        elif i - stack[-1] == max_:
            ans += 1

    elif s[i] == "(":
        stack.append(i)

out = "0 1"
if ans != 0:
    out = f"{max_} {ans}"

sys.stdout.write(out)