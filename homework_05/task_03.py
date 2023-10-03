def generate_squares(*args) -> list:
    return [i ** 2 for i in args]


assert generate_squares(2,3,4) == [4, 9, 16]
assert generate_squares(5,6,7) ==[25, 36, 49]


