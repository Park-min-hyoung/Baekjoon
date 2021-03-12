n = int(input())

data = []
for i in range(n):
    word = input()
    data.append([i, word, len(word)])

data = sorted(data, key=lambda x: (x[2], x[1]))

x = 0
for i in range(n):
    if x != data[i][1]:
        print(data[i][1])
        x = data[i][1]