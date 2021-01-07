n = int(input())

level = []
for i in range(n):
    level.append(int(input()))

cnt = 0
for i in range(n - 1, 0, -1):
    if level[i] <= level[i - 1]:
        temp = level[i - 1]
        while temp >= level[i]:
            temp -= 1
            if temp == 0: break
            else:level[i - 1] = temp
            cnt += 1
for i in range(len(level) - 1):
    if level[i] >= level[i + 1]:
        while level[i] >= level[i + 1]:
            level[i + 1] += 1
            cnt += 1
print(cnt)

'''짧은 소스 코드
n = int(input())

level = []
for i in range(n):
    level.append(int(input()))

cnt = 0
for i in range(n - 1, 0, -1):
    if level[i] <= level[i - 1]:
        cnt += (level[i - 1] - level[i] + 1)
        level[i - 1] = level[i] - 1
print(cnt)'''