def zeroClick(bf):
    cnt = 1
    bf[0] = int(not bf[0])
    bf[1] = int(not bf[1])
    for i in range(1, len(bf)):
        if bf[i - 1] != af[i - 1]:
            cnt += 1
            bf[i - 1] = int(not bf[i - 1])
            bf[i] = int(not bf[i])
            if i != len(bf) - 1:
                bf[i + 1] = int(not bf[i + 1])
    if bf == af:
        return cnt
    else:
        return -1

def zeroNoClick(bf):
    cnt = 0
    for i in range(1, len(bf)):
        if bf[i - 1] != af[i - 1]:
            cnt += 1
            bf[i - 1] = int(not bf[i - 1])
            bf[i] = int(not bf[i])
            if i != len(bf) - 1:
                bf[i + 1] = int(not bf[i + 1])
    if bf == af:
        return cnt
    else:
        return -1

n = int(input())

bf = list(map(int, input()))
af = list(map(int, input()))
res1 = zeroClick(bf[:])
res2 = zeroNoClick(bf[:])

if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)

# 틀렸음
'''나의 해결 : 문제 손도 못뎀'''
'''해결 아이디어
1. 첫번째 전구를 켜는 함수와 켜지 않는 함수를 따로 정의 한다.
2. 두 함수다 두번째 전구부터 시작해 앞의 전구의 현재상태와 목표상태가 다르다면 스위치를 켜주고 똑같다면 켜주지 않는다(마지막에는 i-1, i만 켜준다)
3. 함수 호출을 두 함수에대한 리턴 값을 변수 2개에 각각 저장한다(함수 호출 시 배열자체를 넘겨주면 배열이 변하므로 배열[:]를 넘겨준다)
4. 두 비교값이 모두 0보다 크거나 같으면 두 결과값중 작은것을 선택 나머지는 알아서..'''