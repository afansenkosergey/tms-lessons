def my_filter(condition_func, lst):
    result = []

    for item in lst:
        if condition_func(item):
            result.append(item)

    return result