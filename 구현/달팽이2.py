def dal(x, y):
    d = 0
    data[x][y] = 1
    cnt = 0

    for i in range(n * m - 1):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or data[nx][ny] == 1:
            d += 1
            cnt += 1

            if d == 4:
                d = 0
            nx = x + dx[d]
            ny = y + dy[d]

        if data[nx][ny] == 0:
            data[nx][ny] = 1
            x = nx
            y = ny

    return cnt


n, m = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

data = [[0 for _ in range(m)]for _ in range(n)]

print(dal(0, 0))

'''
문제
1. 표의 바깥 또는 이미 그려진 칸에 닿아서 더 이상 이동할 수 없게 되면, 시계방향으로 선을 꺽어서 그린다
2. 표의 모든 칸이 채워질 때까지, 선을 몇 번 꺾게 될까?

입출력
1. 2 <=M, N <=100
'''