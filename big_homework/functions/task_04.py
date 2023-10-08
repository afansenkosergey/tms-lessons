def compare(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0


assert compare(100, 200) == -1
assert compare(200, 100) == 1
assert compare(100, 100) == 0