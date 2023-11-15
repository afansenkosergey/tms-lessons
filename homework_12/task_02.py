import re


def is_date(date: str) -> bool:
    return bool(re.fullmatch(r'\d{2}-\d{2}-\d{4}', date))


assert is_date('01-12-2022')
assert is_date('55-30-2432')
assert is_date('45-23-2892')
assert is_date('12-45-6745')
assert is_date('67-45-5644')
assert not is_date('12-45-34555')
assert not is_date('123-23-12314')
assert not is_date('12-123-1233')
assert not is_date('122-12-1233')