import re


def is_phone_number(number) -> bool:
    return bool(re.fullmatch(r'\+\d{3} \(\d{2}\) [2(9|5|3|4)]\d{2}-\d{2}-\d{2}', number))


assert is_phone_number('+375 (29) 231-65-19')
assert is_phone_number('+375 (33) 541-12-88')
assert is_phone_number('+375 (44) 375-22-55')
