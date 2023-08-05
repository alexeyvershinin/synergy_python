def main():
    number = int(input("Введите число: "))

    if number == 0:
        print("нулевое число")
    elif number > 0 and number % 2 == 0:
        print("положительное четное число")
    elif number > 0 and number % 2 != 0:
        print("положительное нечетное число")
    elif number < 0 and number % 2 == 0:
        print("отрицательное четное число")
    elif number < 0 and number % 2 != 0:
        print("отрицательное нечетное число")

    if number % 2 != 0:
        print("число не является четным")

if __name__ == '__main__':
    main()

