def my_filter(condition_func, lst):
    for item in lst:
        if condition_func(item):
            yield item