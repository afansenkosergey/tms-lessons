class MyTime:
    def __init__(self, seconds: float):
        self.seconds = seconds

    @property
    def hours(self):
        return int(self.seconds // 3600)

    @property
    def minutes(self):
        return int(self.seconds // 60 % 60)

    def __mul__(self, other) -> 'MyTime':
        return MyTime(self.seconds * other)

    def __truediv__(self, other) -> 'MyTime':
        return MyTime(self.seconds / other)

    def __plus__(self, other: 'MyTime') -> 'MyTime':
        return MyTime(self.seconds + other.seconds)

    def __minus__(self, other: 'MyTime'):
        return MyTime(self.seconds - other.seconds)

    def get_formatted_str(self):
        return f'{self.hours:02d}:{self.minutes:02}:{self.seconds % 60:04.1f}'

    def __str__(self):
        return '"{self.seconds}s'

    def __eq__(self, other: 'MyTime'):
        return self.seconds == other.seconds

    def __ne__(self, other: 'MyTime'):
        return self.seconds != other.seconds

    def __lt__(self, other: 'MyTime') -> bool:
        return self.seconds < other.seconds

    def __gt__(self, other: 'MyTime'):
        return self.seconds > other.seconds

    def __le__(self, other: 'MyTime') -> bool:
        return self.seconds <= other.seconds

    def __ge__(self, other: 'MyTime'):
        return self.seconds >= other.seconds


if __name__ == '__main__':
    time = MyTime(3724.5)
    assert MyTime(15) * 2 == MyTime(30)
    assert MyTime(20) * 2 == MyTime(40)
    assert MyTime(30) / 2 == MyTime(15)
    assert MyTime(40) * 2 == MyTime(80)
    assert MyTime(20) / 2 == MyTime(10)
    assert time.get_formatted_str() == '01:02:04.5'
    assert MyTime(15) < MyTime(16)
    assert MyTime(20) <= MyTime(21)
    assert MyTime(25) <= MyTime(25)
    assert MyTime(17) == MyTime(17)
    assert MyTime(17) != MyTime(16)
    assert MyTime(10) > MyTime(8)
    assert MyTime(15) >= MyTime(13)
    assert MyTime(10) >= MyTime(10)
