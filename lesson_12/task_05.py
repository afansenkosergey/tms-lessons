class SquaresIterable:
    def __init__(self, count):
        self.count = count
        self.current = 1
        self.square_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.square_count >= self.count:
            raise StopIteration
        square = self.current ** 2
        self.current += 1
        self.square_count += 1
        return square


for i in SquaresIterable(10):
    print(i)
