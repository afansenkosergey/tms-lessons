from test_utils import test_sort
import copy


def insertion_sort(lst: list) -> list:
    lst = copy.deepcopy(lst)
    for i in range(1, len(lst)):
        k = lst[i]
        j = i - 1
        while j >= 0 and k < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = k
    return lst


if __name__ == '__main__':
    test_sort(insertion_sort)
