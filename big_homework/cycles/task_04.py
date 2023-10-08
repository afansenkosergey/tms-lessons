lst = [int(i) for i in input().split()]


flag = False
for i in lst:
    if i == 0:
        flag = True
        break
if flag:
    print('yes')
else:
    print('no')