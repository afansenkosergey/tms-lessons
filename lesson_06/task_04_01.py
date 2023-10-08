from functools import reduce
from task_01 import input_list

l = input_list()
result = 0
for num in l:
    result += num
print(result)


result = reduce(lambda x, y: x + y, l , 0)
print(result)