n = int(input())
rop = []

for i in range(n):
    rop.append(int(input()))
rop.sort()

max = 0
for i in range(n):
    if max <= rop[i] * (len(rop) - i):
        max = rop[i] * (len(rop) - i)
print(max)