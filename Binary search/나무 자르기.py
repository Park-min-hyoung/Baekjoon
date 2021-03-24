from sys import stdin

def binary_search(tree, start, end):
    while start <= end:
        mid = (start + end) // 2

        length = 0
        for i in tree:
            if i > mid:
                length += i - mid

        if length >= m:
            value = mid
            start = mid + 1
        else:
            end = mid - 1

    return value


n, m = map(int, stdin.readline().split())
tree = list(map(int, stdin.readline().split()))

print(binary_search(tree, 0, max(tree)))

'''문제
1. 절단기에 높이 H를 지정, 높이를 지정하면 H 높이에서 한줄에 연속해있는 나무를 모두 절단한다.
2. 20, 15, 10, 17이 있을 떄 높이를 15로 지정하면 총 7의 길이의 나무를 집에 가지고 갈것이다.'''