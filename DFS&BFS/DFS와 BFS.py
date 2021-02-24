from collections import deque

def dfs(checked, v, data):
    checked[v] = True
    print(v, end = ' ')

    data[v].sort()
    for i in data[v]:
        if not checked[i]:
            dfs(checked, i, data)

def bfs(checked, v, data):
    queue = deque()
    queue.append(v)
    checked[v] = True

    while queue:
        value = queue.popleft()
        print(value, end = ' ')

        data[value].sort()
        for i in data[value]:
            if not checked[i]:
                queue.append(i)
                checked[i] = True


n, m, v = map(int, input().split())
data = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

checked = [False] * (n + 1)
dfs(checked, v, data)
print()

checked = [False] * (n + 1)
bfs(checked, v, data)