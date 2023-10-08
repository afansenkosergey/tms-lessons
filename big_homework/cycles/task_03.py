lst = [int(i) for i in input().split()]


max_num = lst[0]
for i in lst:
    if i > max_num:
        max_num = i
print(max_num)