n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    a = a % 10

    if a == 0:
        print(10)

    elif a in [1, 5, 6]:
        print(a)

    elif a in [4, 9]:
        b = b % 2
        if b == 0:
            print(a ** 2 % 10)
        else:
            print(a)

    else:
        b = b % 4
        if b == 0:
            print((a ** 4) % 10 % 10 % 10)
        else:
            print((a ** b) % 10 % 10 % 10)

'''
문제
1. 1번 부터 10번까지의 번호를 부여하고, 10대의 컴퓨터가 다음과 같은 방법으로 데이터를 처리
2. 1번 데이터는 1번 컴, 2번 컴퓨터는 2번 컴,......,11번 데이터는 1번 컴
3. 데이터의 개수는 a ^ 개의 형태로 주어진다.
4. 마지막 데이터가 처리될 컴퓨터의 번호를 구하는 프로그램

입출력
1. 1 <= a < 100, 1 <= b < 1,000,000
'''