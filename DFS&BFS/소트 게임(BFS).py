import copy


def bfs(target):
    global cnt
    c_data = copy.deepcopy(data)
    while data[target] != target + 1:
        nx = target + (k - 1)
        if nx >= n:
            continue
        else:
            for i in range(n):
                if i + k - 1 < n and data[i + k - 1] == target + 1:
                    r = data[i:i + k]
                    r.reverse()
                    data[i:i + k] = r
                    cnt += 1

            if c_data == data:
                return -1

            c_data = copy.deepcopy(data)


n, k = map(int, input().split())
data = [int(x) for x in input().split()]
cnt = 0

check = False
for i in range(n):
    if bfs(i) == -1:
        print(-1)
        check = True
        break

if not check:
    print(cnt)

'''문제
1. 소트 게임은 1~N으로 이뤄진 N자리의 순열을 이용(이 게임에선 2보다 크거나 같고 N보다 작거나 같은 수 K가 주어진다)
2. 어떤 수를 뒤집는다고 하면, 그 수부터, 오른쪽으로 총 K개의 수를 뒤집는 것
3. 이 게임을 통해 순열을 오름차순으로 만들려고 한다.'''

https://sosoeasy.tistory.com/32