def main():
    n = int(input('Введите количество чисел: '))
    count = 0

    while n > 0:
        number = int(input('Введите число: '))
        if number == 0:
            count += 1
        n -= 1

    print('Количество введенных чисел равных 0:', count)


if __name__ == '__main__':
    main()
