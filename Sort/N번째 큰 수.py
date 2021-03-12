case = int(input())
for i in range(case):
    data = [int(x) for x in input().split()]
    data.sort(reverse=True)

    print(data[2])