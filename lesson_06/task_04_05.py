def my_reduce(func, lst, initial):
    result = initial

    for item in lst:
        result = func(result, item)

    return result