import re


def is_float_number(number: str) -> bool:
    return bool(re.fullmatch(r'[-+]?[0-9]*\.?[0-9]+', number))


assert is_float_number('-123.342')
assert is_float_number('234.234')
assert is_float_number('234.23423234')
assert is_float_number('-234234.23')
assert is_float_number('-4.234')
assert is_float_number('43123123123123123123.312312312312312312312312')
assert is_float_number('-434532462372572.35472457468578')
assert is_float_number('+43245234523452354.33245234523523452')
assert not is_float_number('234234-234234')
assert not is_float_number('4234234/4234234')
assert not is_float_number('234!34234')
assert not is_float_number('234,4234')
assert not is_float_number('234234+234')
assert not is_float_number('34=234')
assert not is_float_number('2234)234')
assert not is_float_number('2(234')