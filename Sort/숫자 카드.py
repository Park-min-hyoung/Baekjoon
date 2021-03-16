n = int(input())
sang = set(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))

for i in data:
    if i in sang:
        print(1, end=' ')
    else:
        print(0, end=' ')

'''문제
1. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를
구하는 프로그램 '''

'''입,출력
1. 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N
2. 둘째 줄에는 숫자 카드에 적혀 있는 정수가 주어진다.
3. 셋쨰 줄에는 M
4. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야할 M개의 정수가 주어지며,
이 수는 공백으로 구분되어져 있다.'''