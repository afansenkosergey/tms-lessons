def filter_negative_numbers(lst):
    return [num for num in lst if num >= 0]


assert filter_negative_numbers([-2, -1, 0, 1, 2, 3]) == [0, 1, 2, 3]
assert filter_negative_numbers([-20, 15, -10, 0, 10, 20]) == [15, 0, 10, 20]