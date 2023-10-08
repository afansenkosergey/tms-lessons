from task_01 import input_list
from functools import reduce

l = input_list()
l_2 = int(''.join(map(str, l)))
s = 1
for i in range(1, l_2 + 1):
    s *= i
print(s)


result = reduce(lambda x, y: y * x, range(1, l_2 + 1))
print(result)
