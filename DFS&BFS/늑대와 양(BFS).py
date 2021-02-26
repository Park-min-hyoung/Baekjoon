r, c = map(int, input().split())

data = []
for i in range(r):
    data.append(input())

flag = False
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for x in range(r):
    for y in range(c):
        if data[x][y] == 'W':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue

                if data[nx][ny] == 'S':
                    flag = True
                    break

        elif data[x][y] == 'S':
            continue

        elif data[x][y] == '.':
            data[x] = data[x][0:y] + "D" + data[x][y + 1:]

if flag:
    print(0)
else:
    print(1)
    for i in data:
        print(i)

# 틀렸음
'''나의 풀이 : 손도 대지 못했다'''
'''아이디어: 
1. 완전 탐색을 통해 그 공간이 늑대일때는 인접한 곳에 양이 있다면 flag 변수를 True로 바꿔주고 탈출하면 되고 양이면 넘어가고 .이면
울타리를 치면된다.'''