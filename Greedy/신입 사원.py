import sys
input = sys.stdin.readline

case = int(input())

for i in range(case):
    men = int(input())
    test = []
    for j in range(men):
        a, b = map(int, input().split())
        test.append([a, b])

        test = sorted(test, key=lambda a : a[0])

    mi = test[0][1]
    cnt = 0
    for k in range(1, men):
        if mi < test[k][1]:
            cnt += 1
        else:
            mi = test[k][1]
    print(men - cnt)


# 틀렸음
'''나의 해결 : 이번 문제는 많이 어려웠지만 해결하기는 했다. 하지만 내가 한 방법은 시간 초과로 인해 풀리지 않았으니 틀린 것이다.'''
'''아이디어 : 1.다시 풀어보니까 문법이 부족 하기 보다는 아이디어를 못떠올렸다 하나는 오름차순으로 해두고 나보다 서류 성적(첫번째 값) 등수가 높은 사람의
면접 성적(두번째 값) 만 비교해주면 되는데 내가 만약 3등이면 2등이랑 만 비교해주면 된다. 왜냐하면 2등은 1등과 비교해서 이미 최소값을 가져왔기 때문이다.
1등이 제일 낮으면 계속 최소값이 유지 될것이고 2등이 1등 보다 작으면 최소값이 변경되기 때문에 어차피 1등이랑은 굳이 비교해주지 않아도 2등보다 작으면 통과된다
2. 두줄로 나열되었을 때는 하나를 정렬 해줌으로써 나머지 값을 처리하는 것이 효율적이다 그럼 3중 for문도 사용할 필요가 없다'''