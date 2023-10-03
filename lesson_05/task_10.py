def filter_odd_numbers(n: [int]) -> list:
    return [num for num in n if num % 2 == 0]


assert filter_odd_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]