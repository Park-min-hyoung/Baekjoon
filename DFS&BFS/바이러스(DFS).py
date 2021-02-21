def dfs(v_network, v, checked):
    checked[v] = True
    global count
    count += 1

    for i in v_network[v]:
        if not checked[i]:
            dfs(v_network, i, checked)


computer = int(input())
network = int(input())
count = 0

v_network = [[] for _ in range(computer + 1)]
for i in range(network):
    a, b = map(int, input().split())
    v_network[a].append(b)
    v_network[b].append(a)

checked = [False] * (computer + 1)

dfs(v_network, 1, checked)
print(count - 1)