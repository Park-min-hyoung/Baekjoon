def binary_search(money, start, end):
    while start <= end:
        mid = (start + end) // 2

        money_cnt = 1
        cut_money = mid
        for i in money:
            if cut_money < i:
                money_cnt += 1
                cut_money = mid
            else:
                money_cnt += (i // mid)
            cut_money -= i

        if money_cnt > m:
            start = mid + 1
        else:
            end = mid - 1
            res = mid

    return res


n, m = map(int, input().split())
money = list(int(input()) for _ in range(n))

print(binary_search(money, min(money), sum(money)))

#틀렸음
'''나의 해결 : 범위를 잘못 지정했지만 틀린건 틀린거다'''
'''해결 아이디어
1. 초기 탐색 범위의 시작점은 배열의 max 값이고 끝점은 배열의 sum 값이다.
2. 시작점이 배열의 max 값인 이유는 아무리 K(인출금)가 작아도 데이터 하나의 값보다는 크거나 같아야 한다.
(만약 7일 내내 인출 하기 원할때 월요일에 300원을 써야 하는데 인출액이 200원이면 8번을 해줘야 하므로 최소 일주일의 비용중 가장 큰 값은 최소로 가져야 된다)
3. 끝점이 배열의 sum 값인 이유는 sum 값이 7일 동안의 돈을 커버할 수 있기 때문이다(만약 1번만 인출하기 원한다면 mid 값은 배열의 sum 값이다)
'''

'''문제
1. 현우는 아프올 N일 동안 자신이 사용할 금액을 계산, M번만 통장에서 돈을 뺴서 쓰기로 하였다.
2. 현우는 통장에서 K원을 인출하며, 통장에서 뺸 돈으로 하루를 보낼 수 있으면 그대로 사용하고, 모자라게 되면 남은 금액은 통장에 집어넣고 다시
K원을 인출한다.
3. 정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다.'''