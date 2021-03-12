data = []
for i in range(8):
    data.append([i + 1, int(input())])
data = sorted(data, key=lambda x: x[1])

target_data = data[3:8]
target_data.sort()

res = 0
for i in range(5):
    res += target_data[i][1]

print(res)
for i in range(5):
    print(target_data[i][0], end=' ')