from task_01 import input_list

l = input_list()

lis = []
for num in l:
    lis.append(str(num))
print(lis)

lis = [str(num) for num in l]
print(lis)


lis = list(map(str, l))
print(lis)