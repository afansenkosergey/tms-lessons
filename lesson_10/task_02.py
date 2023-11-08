from task_01 import MyTime


class MyTimeInterval:
    def __init__(self, start_seconds, finish_seconds):
        self.start = MyTime(start_seconds)
        self.finish = MyTime(finish_seconds)

    def is_inside(self, time):
        return self.start <= time <= self.finish

    def intersects(self, other):
        return self.is_inside(other.start) or self.is_inside(other.finish) or \
            other.is_inside(self.start) or other.is_inside(self.finish)


if __name__ == '__main__':
    interval = MyTimeInterval(5, 13)

    assert interval.is_inside(MyTime(5))
    assert interval.is_inside(MyTime(6))
    assert interval.is_inside(MyTime(9))
    assert interval.is_inside(MyTime(13))
    assert not interval.is_inside(MyTime(3))
    assert not interval.is_inside(MyTime(4))
    assert not interval.is_inside(MyTime(14))
    assert not interval.is_inside(MyTime(17))

    assert interval.intersects(MyTimeInterval(0, 5))
    assert interval.intersects(MyTimeInterval(3, 13))
    assert interval.intersects(MyTimeInterval(9, 19))
    assert interval.intersects(MyTimeInterval(13, 15))
    assert not interval.intersects(MyTimeInterval(0, 4))
    assert not interval.intersects(MyTimeInterval(1, 3))
    assert not interval.intersects(MyTimeInterval(14, 19))
    assert not interval.intersects(MyTimeInterval(15, 25))
