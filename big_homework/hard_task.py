def is_magic_square(matrix):
    n = len(matrix)
    sum_first_row = sum(matrix[0])

    ''''Список суммы строк'''
    row_sums = [sum(row) for row in matrix]

    '''Список суммы столбцов'''
    col_sums = [sum(matrix[i][j] for i in range(n)) for j in range(n)]

    '''Сумма первой диагонали'''
    primary_diagonal_sum = sum(matrix[i][i] for i in range(n))

    '''Сумма второй диагонали'''
    secondary_diagonal_sum = sum(matrix[i][n - i - 1] for i in range(n))

    return all(
        all_sum == sum_first_row for all_sum in row_sums + col_sums + [primary_diagonal_sum, secondary_diagonal_sum])


input_size_matrix = int(input("Enter the size of the square matrix: "))

matrix_list = []
print("Enter matrix:")
for _ in range(input_size_matrix):
    row = list(map(int, input().split()))
    matrix_list.append(row)

if is_magic_square(matrix_list):
    print(True)
else:
    print(False)
