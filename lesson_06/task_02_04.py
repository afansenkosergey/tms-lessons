def my_map(func, lst):
    l = []
    for num in lst:
        l.append(func(num))
    return l