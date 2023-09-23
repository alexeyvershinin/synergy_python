def main():
    n = int(input("Введите количество чисел: "))
    if not 1 <= n <= 100000:
        raise ValueError("Количество чисел должно быть в диапазоне от 1 до 100000")

    numbers = list(map(int, input().split()))
    numbers_set = set(numbers[:n])
    number_of_different_numbers = len(numbers_set)

    print(number_of_different_numbers)


if __name__ == "__main__":
    main()
