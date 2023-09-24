import random


def generate_metrix(rows, columns):
    return [[random.randint(-100, 100) for _ in (range(columns))] for _ in (range(rows))]


def get_summ_matrix(matrix_1, matrix_2):
    result_matrix = []
    for i in range(len(matrix_1)):
        result_row = []

        for j in range(len(matrix_1[0])):
            sum_element = matrix_1[i][j] + matrix_2[i][j]
            result_row.append(sum_element)
        result_matrix.append(result_row)
    return result_matrix


def main():
    rows = int(input('Введите количество строк матрицы: '))
    columns = int(input('Введите количество колонок матрицы: '))

    matrix_1 = generate_metrix(rows, columns)
    matrix_2 = generate_metrix(rows, columns)

    result_matrix = get_summ_matrix(matrix_1, matrix_2)

    print(matrix_1)
    print(matrix_2)
    print(result_matrix)


if __name__ == "__main__":
    main()
