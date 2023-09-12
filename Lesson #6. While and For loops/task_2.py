def main():
    n = int(input("Введите натуральное число N: "))

    divisors = 0

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors += 1
            if i != n // i:
                divisors += 1

    print(f"Количество натуральных делителей числа {n} равно {divisors}")

if __name__ == '__main__':
    main()
