case = int(input())

for i in range(case):
    num = int(input())
    tree = list(map(int, input().split()))
    tree.sort()

    retree = [0 for _ in range(len(tree))]
    cnt = 0
    for j in range(len(retree)):
        if j % 2 == 0:
            retree[cnt] = tree[j]
        else:
            retree[len(retree) - 1 - cnt] = tree[j]
            cnt += 1

    mi = abs(retree[len(retree) - 1] - retree[0])
    for j in range(len(retree) - 1):
        if mi < abs(retree[j] - retree[j + 1]):
            mi = abs(retree[j] - retree[j + 1])
    print(mi)

'''쉽게 하는 방법
case = int(input())

for i in range(case):
    num = int(input())
    tree = list(map(int, input().split()))
    tree.sort()
    
    result = 0
    for j in range(2, num):
        result = max(result, abs(tree[j] - tree[j - 2]))
    print(result)
    
    아이디어
    1. 예를 들어 1, 2, 3, 4, 5(1이 제일큼) 중에 가장 큰 것을 중간에 두고 그 다음은 순서대로 왼쪽 오른쪽으로 나열하면 4 2 1 3 5가 되는데
    이것을 잘 살펴보면 서로 인접한 통나무 사이의 높이의 차값의 최대값이 2이므로 2이 애들만 체크해주면된다.
    2. 그러므로 오름차순을 통해 간격 2를 두고 체킹해주면 된다.
'''