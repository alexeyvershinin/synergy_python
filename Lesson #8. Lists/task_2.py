def main():
    N = int(input('Введите количество чисел: '))
    numbers = list(map(int, input('Введите числа через пробел: ').split()))
    modified_numbers = [0] * N

    for i in range(N):
        modified_numbers[i] = numbers[(N - 1 - i) % N]

    print(*modified_numbers)

if __name__ == "__main__":
    main()
