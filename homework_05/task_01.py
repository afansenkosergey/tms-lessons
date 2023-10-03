def is_year_leap(year: int) -> bool:
    if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
        return True
    else:
        return False


assert is_year_leap(2000) == False
assert is_year_leap(2002) == False
assert is_year_leap(1700) == False
assert is_year_leap(2003) == False
assert is_year_leap(2004) == True
assert is_year_leap(2005) == False
assert is_year_leap(2100) == False
assert is_year_leap(2007) == False
assert is_year_leap(2008) == True
