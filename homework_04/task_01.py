s = 0
for i in range(0, 101, 5):
    s += i
    print(i)


s_1 = 0
for j in range(0, 101, 1):
    s_1 += j
    if j % 5 == 0:
        print(j)