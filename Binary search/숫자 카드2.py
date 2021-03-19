from sys import stdin

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return array[start:end + 1].count(target)
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


n = int(input())
array = sorted(list(map(int, stdin.readline().split())))
m = int(input())
rq_array = list(map(int, stdin.readline().split()))

dic = {}
for target in array:
    if target not in dic:
        dic[target] = binary_search(array, target, 0, n - 1)

for target in rq_array:
    if target in dic:
        print(dic[target], end=' ')
    else:
        print(0, end=' ')


#틀렸음
'''나의 해결 : 못 풀었다'''
'''해결 아이디어
1. 한줄 입력 받을떄는 시간 초과를 방지하기 위해 from sys import stdin을 선언하고 stdin.readline().split() 사용
2. 이분 탐색을 하긴 하는데 dict(사전)자료형을 사용해서 dict에 key 값이 없을때만 이분탐색이 되도록 한다
3. 이분 탐색시에 target과 일치하는 값을 찾았다면 그 때 start ~ end 사이에 target과 같은 값이 있는지 count 메소드를 통해 찾아준다
그러므로 전체 찾아보지 않고 줄어든 범위안에서만 찾으므로 시간을 절약할 수 있다'''

'''문제
1. 상근이는 숫자 카드 N개를 가지고 있다.
2. 정수 M개가 주어졌을떄, 이 수가 적혀있는 숫자 카드를 상근이가 몇개 가지고 있는지 구하는 프로그램을 작성하시오'''