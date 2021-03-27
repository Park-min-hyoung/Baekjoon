from sys import stdin

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2

        blue_cnt = 1
        lesson_sum = 0
        for i in array:
            if lesson_sum + i > mid:
                lesson_sum = 0
                blue_cnt += 1

            lesson_sum += i

        if blue_cnt > m:
            start = mid + 1
        else:
            res = mid
            end = mid - 1

    return res


n, m = map(int, stdin.readline().split())
array = list(map(int, stdin.readline().split()))

print(binary_search(array, max(array) // m, sum(array)))

# 틀렸음
'''나의 해결 : 범위를 정하는데 있어서 틀렸다 그것도 틀린거다'''
'''해결 아이디어
1. mid 값(블루레이 영상 길이)을 정해준 후 배열의 값을 더해봄으로써 필요한 블루레이 개수를 구한다.
9 3
1 2 3 4 5 6 7 8 9
2. 시작점을 배열의 max 값으로 해준 이유는 만약 위의 예제에서 9개의 블루레이를 가지고 있다면 배열에서 가장 큰 값인 9를 담아야하므로 max 값으로 해줘야 한다
(내가 했던 sum // m(m이 9일때 > 평균 값 = 5)으로는 6 7 8 9를 담지 못한다.
3. 끝점은 배열의 sum 값으로 지정해준다(블루레이가 1개일때 모두 한꺼번에 담아야 하기 때문이다)'''

'''문제
1. 블루레이에는 총 N개의 레슨이 들어가는데, 블루레이를 녹화할 때, 레슨의 순서가
바뀌면 안된다.(즉 i번 레슨과 j번 레슨을 같은 블루레이에 녹화하려면 i와 j 사이의
모든 레슨도 같은 블루레이에 녹화해야한다.)
2. M개의 블루레이에 모든 기타 레슨 동영상을 녹화하기로 결정
(이때, 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고한다
단, M개의 블루레이는 모두 같은 크기)
3. 가능한 블루레이의 크기 중 최소를 구하는 프로그램'''