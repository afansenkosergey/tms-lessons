def generate_squares(count):
    current = 1
    square_count = 0
    while square_count < count:
        yield current ** 2
        current += 1
        square_count += 1


for i in generate_squares(10):
    print(i)
