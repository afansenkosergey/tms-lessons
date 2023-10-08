from task_01 import input_list

l = input_list()

lis = []
lis_1 = []
lis_2 = []
for num in l:
    if num % 2 == 0:
        lis.append(num)
    if num == 0:
        lis_1.append(num)
    if num < 0:
        lis_2.append(num)
print(len(lis))
print(len(lis_1))
print(len(lis_2))

lis = [num for num in l if num % 2 == 0]
lis_1 = [num for num in l if num == 0]
lis_2 = [num for num in l if num < 0]

print(len(lis))
print(len(lis_1))
print(len(lis_2))


lis_1 = list(filter(lambda num: num % 2 == 0, l))
lis_2 = list(filter(lambda num: num == 0, l))
lis_3 = list(filter(lambda num: num < 0, l))


print(len(lis_1))
print(len(lis_2))
print(len(lis_3))