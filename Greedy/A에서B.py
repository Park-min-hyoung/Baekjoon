a, b = input().split()
result = int(b)

count = 0
while int(a) != result:
    count += 1
    if result < int(a):
        count = -2
        break
    if b[len(b) - 1] == '1':
        b = b[:len(b) - 1]
        result = int(b)
    elif result % 2 == 0:
        result //= 2
        b = str(result)
    else:
        count = -2
        break

print(count + 1)