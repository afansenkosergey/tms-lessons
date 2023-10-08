from task_01 import input_list


l = input_list()
lis = []
for num in l:
    lis.append(round(num / 100))
print(lis)

lis = [round(num / 100) for num in l]
print(lis)


lis = list(map(lambda num: round(num / 100), l))
print(lis)