case = int(input())

for i in range(case):
    a, b = [0] * 26, [0] * 26

    ia, ib = input().split()

    for i in ia:
        a[ord(i) - 97] += 1

    for i in ib:
        b[ord(i) - 97] += 1

    if a == b:
        print(ia + " & " + ib + " are anagrams.")
    else:
        print(ia + " & " + ib + " are NOT anagrams.")