def main():
    unique_numbers = set()
    sequence = list(map(int, input('Введите последовательность чисел через пробел: ').split()))

    for number in sequence:
        if number in unique_numbers:
            print(number, 'YES')
        else:
            print(number, 'NO')

        unique_numbers.add(number)


if __name__ == "__main__":
    main()
