from task_01 import input_list

l = input_list()

lis = []
for num in l:
    if num >= 0:
        lis.append(num)
print(lis)


lis = [num for num in l if num >= 0]
print(lis)

lis = (list(filter(lambda num: num >= 0, l)))
print(lis)