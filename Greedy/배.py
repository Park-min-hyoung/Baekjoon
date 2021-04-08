n = int(input())
crain_weight = list(map(int, input().split()))
crain_weight.sort()

m = int(input())
box_weight = list(map(int, input().split()))
box_weight.sort()

if max(box_weight) > max(crain_weight):
    print(-1)

t = 0
time = 1
for i in range(m):
    if t == n:
        t = 0
        time += 1
    if crain_weight[t] >= box_weight[i]:
        t += 1
    else:
        for j in range(n):
            if crain_weight[j] >= box_weight[i]:
                t = j + 1
                break
    print(t)
    print(time, 999)

print(time)

'''문제
1. 모든 화물은 박스 안에 넣어져 있다.
2. 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다.(모든 크레인은 동시에 움직인다)
3. 각 크레인은 무게 제한이 있고 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다.
4. 모든 박스를 배로 옮기는데 드는 시간의 최소값을 구하는 프로그램을 작성하시오
3
6 8 9
5
2 5 2 4 7'''