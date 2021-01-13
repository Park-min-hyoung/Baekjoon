case = int(input())
for i in range(case):
    n = int(input())
    fibo = [0, 1]
    i = 2
    while True:
        if fibo[i - 1] + fibo[i - 2] > n:
            break
        fibo.append(fibo[i - 1] + fibo[i - 2])
        i += 1

    sum = 0
    sumlist = []
    for j in range(len(fibo) - 1, 0, -1):
        if sum + fibo[j] <= n:
            sum += fibo[j]
            sumlist.append(fibo[j])
            sumlist.sort()

    for j in range(len(sumlist)):
        print(sumlist[j], end = ' ')
    print()