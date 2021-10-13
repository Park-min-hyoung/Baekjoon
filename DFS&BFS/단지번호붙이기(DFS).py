from sys import stdin

def dfs(i, j):
    data[i][j] = target + 1
    global cnt
    cnt += 1

    if j + 1 < n and data[i][j + 1] == 1:
        dfs(i, j + 1)
    if i + 1 < n and data[i + 1][j] == 1:
        dfs(i + 1, j)
    if j - 1 >= 0 and data[i][j - 1] == 1:
        dfs(i, j - 1)
    if i - 1 >= 0 and data[i - 1][j] == 1:
        dfs(i - 1, j)


n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, stdin.readline().rstrip())))

target = 1
cnt = 0
nums = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            dfs(i, j)
            nums.append(cnt)
            target += 1
            cnt = 0

nums.sort()
print(target - 1)
for value in nums:
    print(value)