def main():
    def factorial(n):
        if n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

    def factorial_list(n):
        result_list = []
        while n >= 1:
            result_list.append(factorial(n))
            n -= 1
        return result_list

    n = int(input("Введите натуральное целое число: "))

    if n >= 0:
        factorials = factorial_list(factorial(n))
        print(factorials)
    else:
        print("Введите корректное натуральное число.")


if __name__ == "__main__":
    main()
