from test_utils import test_sort
import copy


def merge_sort(lst: list) -> list:
    if len(lst) < 2:
        return lst[:]
    else:
        lst = copy.deepcopy(lst)
        center = len(lst) / 2
        left = merge_sort[:center]
        right = merge_sort[center:]
    return


if __name__ == '__main__':
    test_sort(merge_sort)
