import sys
input = sys.stdin.readline
from collections import deque


def bfs(checked, start, data):
    cnt = 0
    queue = deque()

    queue.append(start)
    checked[start] = True

    while queue:
        v = queue.popleft()
        cnt += 1
        for i in data[v]:
            if not checked[i]:
                checked[i] = True
                queue.append(i)

    return cnt


n, m = map(int, input().split())

data = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    data[b].append(a)

value = []
for i in range(1, n + 1):
    checked = [False] * (n + 1)
    value.append(bfs(checked, i, data))

max_cnt = max(value)
for i in range(len(value)):
    if max_cnt == value[i]:
        print(i + 1, end = ' ')

'''문제
1. 한 번의 해킹으로 여러개의 컴퓨터를 해킹 한다
2. 이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있다.(A가 B를 신뢰하는 경우에 B를 해킹하면 A도 해킹 된다)
3. 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력'''