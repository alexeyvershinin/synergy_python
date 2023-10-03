def main():
    N = int(input('Введите количество чисел: '))
    numbers = list(map(int, input('Введите числа через пробел: ').split()))

    last_element = numbers[-1]

    for i in range(N - 1, 0, -1):
        numbers[i] = numbers[i - 1]

    numbers[0] = last_element

    print(*numbers)

if __name__ == "__main__":
    main()
