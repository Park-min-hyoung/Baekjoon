def dfs(checked, v, data):
    checked[v] = True

    global count1
    global count2

    count2 += 1
    if v == second:
        count1 = count2

    for i in data[v]:
        if not checked[i]:
            dfs(checked, i, data)


n = int(input())
first, second = map(int, input().split())

m = int(input())
data = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

checked = [False] * (n + 1)
count1 = 0
count2 = 0

dfs(checked, m, data)
print(count1 - 1)


'''입력
1. 사람들은 연속된 번호로 각각 표시된다.
2. 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호
3. 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다.
4. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x, y가 각 줄에 나온다.'''