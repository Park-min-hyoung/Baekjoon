import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    test = copy.deepcopy(white)

    if test[x][y] == '*':
        test[x][y] = '.'
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < 3 and 0 <= ny and ny < 3:
                if test[nx][ny] == '.':
                    test[nx][ny] = '*'
                else:
                    test[nx][ny] = '.'
    else:
        test[x][y] = '*'
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx and nx < 3 and 0 <= ny and ny < 3:
                if test[nx][ny] == '.':
                    test[nx][ny] = '*'
                else:
                    test[nx][ny] = '.'

    if test == data:
        return True

    return False


def check():
    res = 0
    for i in range(3):
        for j in range(3):
            if bfs(i, j) == True:
                res += 1



white = [list(['.' for _ in range(3)]) for _ in range(3)]
case = int(input())
for i in range(case):

    data = [list([x for x in input()]) for _ in range(3)]

    check()
print(res)

#틀렸음
'''나의 해결 : 손도 데지 못했다'''
'''나중에 풀어야지'''

'''문제
1. 어떤 칸을 클릭한다면 당신이 클릭한 칸과 그 칸에 인접한 동서남북 네 칸이 색이 바뀐다
2. 모든 칸이 흰색인 3x3 보드를 입력으로 주어지는 보드의 형태로 바꾸려고 한다.'''