def generate_natural_cubes(n: int) -> list:
    return [i ** 3 for i in range(1, n + 1)]


assert generate_natural_cubes(3) == [1, 8, 27]
assert generate_natural_cubes(7) == [1, 8, 27, 64, 125, 216, 343]

