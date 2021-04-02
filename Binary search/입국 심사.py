def binary_search(time, start, end):
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for t in time:
            cnt += mid // t
        # cnt > m 일때는 mid(시간)가 크므로 다음 mid가 작아지기 위해 end 값을 조정해준다.(mid를 줄여준다)
        if cnt >= m:
            end = mid - 1
            res = mid
        # cnt < m 일때는 mid(시간)가 작으므로 다음 mid가 커지기 위해 start 값을 조정해준다.
        else:
            start = mid + 1

    return res


n, m = map(int, input().split())

time = []
for _ in range(n):
    time.append(int(input()))

print(binary_search(time, min(time), max(time) * m))

# 틀렸음
'''나의 해결 : 손도 대지 못했다'''
'''해결 아이디어
1. 시작점을 min(time)으로 해주는 이유는 1명만 입국 심사를 받을때 가장 짧게 끝내는 심사원에게 심사 받기 위해서이다.
2. 끝점을 max(time) * m 으로 해주는 이유는 m명이 입국 심사를 받을때 가장 길게 끝내는 심사원에게 모두 심사 받을 수도 있기 때문이다.
3. 시간을 mid 값으로 정하고 for 문을 통해 mid // 각 심사대의 time 한 값을 for 문이 끝날때 까지 cnt에 계속 합해준다.
4. end(mid가 작아진다)를 건드리는 조건문에서는 최소값 start(mid가 커진다)를 건드리는 조건문에서는 최대값을 구하면된다.'''

'''문제
1, 상근이와 친구들은 총 M명이고 지금 공항에서 한 줄로 서서 입국심사를 기다리고 있는 상황(입국 심사대는 총 N개)
2. 각 입국심사관이 심사를 하는데 걸리는 시간은 사람마다 모두 다르다(k번 심사대에 앉아 있는 심사관이 한명을 심사를 하는데 드는 시간 = Tk)
3. 한 심사대에서는 한 번에 한 사람만 심사를 할 수 있고 가장 앞에 서 있는 사람은 비어있는 심사대가 보이면 거기로 가서 심사를 받을 수 있다.
4. 하지만 항상 이동을 해야 하는 것은 아니고 더 빠른 심사대의 심사가 끝나길 기다린 다음에 그 곳으로 가서 심사를 받아도 된다.
5. 7 10 14 (20으로 가지않고 1초 기다렸다가 받으면 28초 아니면 30초에 끝나)'''