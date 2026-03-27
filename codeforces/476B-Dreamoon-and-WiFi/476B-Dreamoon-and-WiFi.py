import sys
input = sys.stdin.readline
s1 = list(input().strip())
s2 = list(input().strip())
n = len(s2)

sum_ = 0
for char in s1:
    sum_ += (1 if char == "+" else -1)

count = 0
total_count = 0
def backtrack(pos, index):
    global total_count
    global count
    if index == n:
        total_count += 1
        count += (1 if pos == sum_ else 0)
        return

    if s2[index] == "?":
        pos += 1
        backtrack(pos, index + 1)
        pos -= 2
        backtrack(pos, index + 1)
    else:
        pos += (1 if s2[index] == "+" else -1)
        backtrack(pos, index + 1)

backtrack(0, 0)
sys.stdout.write(str(count / total_count))