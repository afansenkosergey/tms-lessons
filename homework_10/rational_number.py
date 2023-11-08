class Rational:
    def __init__(self, __numerator, __denominator):
        self.__numerator = __numerator
        self.__denominator = __denominator
        self.__normalize()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'

    def __mul__(self, other: 'Rational') -> 'Rational':
        new_numerator = self.__numerator * other.numerator
        new_denominator = self.__denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, other: 'Rational') -> 'Rational':
        new_numerator = self.__numerator * other.denominator
        new_denominator = self.__denominator * other.numerator
        return Rational(new_numerator, new_denominator)

    def __add__(self, other: 'Rational') -> 'Rational':
        new_numerator = self.__numerator * other.denominator + other.numerator * self.__denominator
        new_denominator = self.__denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other: 'Rational') -> 'Rational':
        new_numerator = self.__numerator * other.denominator - other.numerator * self.__denominator
        new_denominator = self.__denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __eq__(self, other: 'Rational') -> bool:
        return self.__numerator == other.numerator and self.__denominator == other.denominator

    def __ne__(self, other: 'Rational') -> bool:
        return not (self == other)

    def __ge__(self, other: 'Rational') -> bool:
        return self.__numerator * other.denominator >= other.numerator * self.__denominator

    def __le__(self, other: 'Rational') -> bool:
        return self.__numerator * other.denominator <= other.numerator * self.__denominator

    def __gt__(self, other: 'Rational') -> bool:
        return self.__numerator * other.denominator > other.numerator * self.__denominator

    def __lt__(self, other: 'Rational') -> bool:
        return self.__numerator * other.denominator < other.numerator * self.__denominator

    def __normalize(self):
        common_divisor = self.gcd(abs(self.__numerator), abs(self.__denominator))
        self.__numerator //= common_divisor
        self.__denominator //= common_divisor
        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

    @staticmethod
    def gcd(a, b: int) -> int:
        while b:
            a, b = b, a % b
        return a


if __name__ == '__main__':
    first = Rational(7, 2)
    second = Rational(9, 3)

    assert str(second) == '3 / 1'
    assert first + second == Rational(13, 2)
    assert first - second == Rational(1, 2)
    assert first / second == Rational(7, 6)
    assert first * second == Rational(21, 2)

    assert Rational(24, 2) == Rational(12, 1)
    assert Rational(24, 2) != Rational(12, 3)

    assert Rational(12, 4) <= Rational(8, 2)
    assert Rational(4, 2) <= Rational(15, 3)

    assert Rational(8, 2) >= Rational(12, 4)
    assert Rational(12, 3) >= Rational(12, 3)

    assert Rational(4, 6) < Rational(2, 1)
    assert Rational(3, 3) > Rational(2, 8)

    assert Rational(-5, -2) == Rational(5, 2)

    a = Rational(1, 4)
    b = Rational(3, 2)
    c = Rational(1, 8)
    d = Rational(156, 100)
    assert a * (b + c) + d == Rational(1573, 800)
