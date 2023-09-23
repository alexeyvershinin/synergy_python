def main():
    n = int(input("Введите количество чисел: "))
    count = 1
    lst = []

    while count <= n:
        number = int(input("Введите число: "))
        lst.append(number)
        count += 1

    print(*lst[::-1])

if __name__ == "__main__":
    main()
