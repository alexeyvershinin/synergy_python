def main():
    a = int(input('Введите число A: '))
    b = int(input('Введите число B: '))

    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=' ')

if __name__ == '__main__':
    main()
