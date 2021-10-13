from sys import stdin

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, stdin.readline().split())))

time = 1
before_time = 0
fail = []
check = False
while True:
    if time == before_time:
        break

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if data[i][j] == 1:
                if i - 1 >= 0 and data[i - 1][j] == 0:
                    fail.append((i, j))
                    continue
                elif j - 1 >= 0 and data[i][j - 1] == 0:
                    fail.append((i, j))
                    continue
                elif i + 1 < n and data[i + 1][j] == 0:
                    fail.append((i, j))
                    continue
                elif j + 1 < m and data[i][j + 1] == 0:
                    fail.append((i, j))
                    continue
                check = True

    for remove in fail:
        i = remove[0]
        j = remove[1]
        print(i, j)
        data[i][j] = 0

    if check:
        time += 1
        before_time = time
        check = False

for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()