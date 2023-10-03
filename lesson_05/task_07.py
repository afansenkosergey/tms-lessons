def sum_and_max(*args):
    return sum(args), max(args)


assert sum_and_max(1, 2 ,3) == (6, 3)
assert sum_and_max(4, 5, 6) == (15, 6)
assert sum_and_max(7, 8, 9) == (24, 9)
