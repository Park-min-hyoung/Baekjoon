import sys
sys.setrecursionlimit(50000)

def dfs(x, y, m, n):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False

    if data[x][y] == 1:
        data[x][y] = 0
        dfs(x + 1, y, m, n)
        dfs(x - 1, y, m, n)
        dfs(x, y + 1, m, n)
        dfs(x, y - 1, m, n)
        return True

    return False


case = int(input())
for i in range(case):
    n, m, k = map(int, input().split())
    data = [[0] * n for _ in range(m)]

    for j in range(k):
        a, b = map(int, input().split())
        data[b][a] = 1

    res = 0
    for x in range(m):
        for y in range(n):
            if dfs(x, y, m, n) == True:
                res += 1

    print(res)

# 틀렸음
'''나의 풀이 : 틀렸음'''
'''아이디어: 
1. 나동빈님의 얼음 얼리기 문제라 똑같다
2. 재귀 깊이가 깊게 들어가면 sys.setrecursionlimit(50000)를 통해 재귀 제한 높이 설정을 해줘야 한다'''

'''문제
1. 어떤 배추에 배추 흰지렁이가 한마리라도 살고 잇으면 이 지렁이는 인접한 다른 배추로 이동 해서 그 배추를도 해충으로 부터 보호
2. '''

'''입력
1. 1 ≤ 가로 길이 ≤ 50, 1 ≤ 세로 길이 ≤ 50 1 <= 배추 개수 <= 2500'''