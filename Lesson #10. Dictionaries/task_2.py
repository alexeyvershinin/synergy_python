def main():
    digits = {}

    for i in range(10, - 6, -1):
        digits[i] = i ** i

    print(digits)


if __name__ == '__main__':
    main()
