from functools import reduce
from task_01 import input_list

l = input_list()

max_number = max(l)
print(max_number)


max_number= reduce(lambda x, y: x if x > y else y, l)
print(max_number)