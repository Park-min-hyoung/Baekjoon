n = int(input())

data = []
for i in range(n):
    na, cnt, score = map(int, input().split())
    data.append([na, cnt, score])

data = sorted(data, key=lambda x: -x[2])
ma = data[0][0]
three_cnt = 0
check_cnt = 0
for i in range(len(data)):
    if ma == data[i][0]:
        three_cnt += 1

    if three_cnt > 2:
        three_cnt = 0
        continue

    print(data[i][0], data[i][1])
    check_cnt += 1
    if check_cnt == 3:
        break