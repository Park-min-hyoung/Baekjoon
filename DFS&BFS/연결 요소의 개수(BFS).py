from collections import deque


def bfs(checked, start, data):
    queue = deque()
    queue.append(start)
    checked[start] = True

    global cnt
    cnt += 1

    while queue:
        value = queue.popleft()

        for i in data[value]:
            if not checked[i]:
                queue.append(i)
                checked[i] = True


n, m = map(int, input().split())

data = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

checked = [False] * (n + 1)
checked[0] = True
cnt = 0

while True:
    v = 0
    for i in range(len(checked)):
        if not checked[i]:
            v = i
            break
    bfs(checked, v, data)

    if False not in checked:
        break

print(cnt)