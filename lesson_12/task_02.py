import re


def is_car_number(number: str) -> bool:
    return bool(re.fullmatch(r'\d{4}[A-Z]{2}-\d', number))


assert is_car_number('1234AB-5')
assert is_car_number('1212FF-2')
assert not is_car_number('1212SS-A')
assert not is_car_number('11212AA-5')
