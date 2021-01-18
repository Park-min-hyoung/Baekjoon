a = int(input())
b = int(input())
c = int(input())
t = a + b + c

if a == 60 and b == 60 and c == 60: print("Equilateral")
elif t == 180:
    if a == b or a == c or b == c: print("Isosceles")
    else: print("Scalene")
else: print("Error")