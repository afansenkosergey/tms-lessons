def get_natural_numbers(n: [int]) -> list:
    return [i for i in range(1, n + 1)]

assert get_natural_numbers(3) == [1, 2, 3]
assert get_natural_numbers(7) == [1, 2, 3, 4, 5, 6, 7]
