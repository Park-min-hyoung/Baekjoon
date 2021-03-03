from collections import deque

def bfs(checked, start, data):
    queue = deque()
    queue.append(start)
    checked[start] = True

    while queue:
        v = queue.popleft()

        for i in data[v]:
            if not checked[i]:
                queue.append(i)
                result[i] = result[v] + 1
                checked[i] = True


n = int(input())
first, second = map(int, input().split())

m = int(input())
data = [[] for _ in range(n + 1)]
result = [0 for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

checked = [False] * (n + 1)

bfs(checked, first, data)

if result[second] != 0: print(result[second])
else: print(-1)

# 틀렸음
'''나의 해결 : BFS는 비슷했지만 누적된 값을 가져오는 것은 실패했다.'''
'''아이디어: 
1. BFS 문제랑 비슷한데 누적된 값을 저장하는 배열과 방법만 알기만 하면 된다.
'''


'''입력
1. 사람들은 연속된 번호로 각각 표시된다.
2. 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호
3. 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다.
4. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x, y가 각 줄에 나온다.'''