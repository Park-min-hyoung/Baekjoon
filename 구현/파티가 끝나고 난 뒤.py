n, m = map(int, input().split())
news = map(int, input().split())

for i in news:
    print(i - n * m, end = ' ')