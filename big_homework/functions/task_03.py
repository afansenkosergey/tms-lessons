def simple_compare(x, y):
    return x < y


assert simple_compare(1, 2) == True
assert simple_compare(2, 1) == False
assert simple_compare(1, 1) == False