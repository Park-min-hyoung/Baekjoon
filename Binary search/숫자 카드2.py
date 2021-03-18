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
array = list(map(int, input().split()))
array.sort()
m = int(input())
rq_array = list(map(int, input().split()))

for target in rq_array:
    res = binary_search(array, target, 0, n)

    if res == None:
        print(0, end=' ')
    else:
        print(res, end=' ')




'''문제
1. 상근이는 숫자 카드 N개를 가지고 있다.
2. 정수 M개가 주어졌을떄, 이 수가 적혀있는 숫자 카드를 상근이가 몇개 가지고 있는지 구하는 프로그램을 작성하시오'''