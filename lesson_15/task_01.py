from test_utils import test_sort
import copy


def buble_sort(lst: list) -> list:
    lst = copy.deepcopy(lst)
    for _ in range(len(lst)):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


if __name__ == '__main__':
    test_sort(buble_sort)
