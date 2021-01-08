n = int(input())

for i in range(n):
    cnt = 0
    os = int(input())
    before = list(input())
    after = list(input())
    before_list = []
    after_list = []

    for j in range(os):
        if before[j] != after[j]:
            before_list.append(before[j])
            after_list.append(after[j])

    before_list.sort()
    after_list.sort()
    for j in range(len(before_list)):
        if before_list[j] == after_list[j]:
            cnt += 0.5
        else:
            cnt += 1
    print(int(cnt))

# 틀렸음
'''나의 해결 : 입력값은 넣은 대로 출력이 제대로 됬는데 이번에도 왜 안되는지 모르겠다다
1. 지금 상태와 목적 상태가 다른 인자는 각각 배열에 넣어준다
2. 오름차순을 해준다
3. 각각 오름차순 된 두 배열의 요소 값이 같으면 분명히 반대되는 문자도 같은 값이 있을 것이기 때문에 0.5를 더해주고 같지 않으면 1을 더해준다
4. 진짜 이런것을 어떻게 생각해낼까 대단한 사람인 것 같다'''