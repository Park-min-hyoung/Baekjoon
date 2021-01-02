n = int(input())
time = [int(x) for x in input().split()]
time.sort()

sum = 0
for i in range(len(time)):
    for j in range(i + 1):
        sum += time[j]
print(sum)