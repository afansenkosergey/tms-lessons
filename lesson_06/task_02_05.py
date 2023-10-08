def my_map(func, lst):
    for item in lst:
        yield func(item)