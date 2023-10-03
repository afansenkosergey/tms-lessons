def list_sum(l: int) -> list:
    count = 0
    for elem in l:
        count += elem
    return count


assert list_sum([1, 2, 3]) == 6
assert list_sum([1, 2]) == 3
assert list_sum([]) == 0