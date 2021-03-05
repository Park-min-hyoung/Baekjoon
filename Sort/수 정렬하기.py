n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

for i in range(n):
    for j in range(n):
        if data[j] > data[i]:
            data[i], data[j] = data[j], data[i]

for i in data:
    print(i)