chess = list(map(int, input().split()))

default = [1, 1, 2, 2, 2, 8]

for i in range(len(chess)):
    print(default[i] - chess[i], end = ' ')