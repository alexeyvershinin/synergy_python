def main():
    list1 = set()
    n = int(input("Введите количество чисел в первом списке: "))
    for _ in range(n):
        num = int(input())
        list1.add(num)

    list2 = set()
    m = int(input("Введите количество чисел во втором списке: "))
    for _ in range(m):
        num = int(input())
        list2.add(num)

    common_numbers = list1.intersection(list2)
    count_common = len(common_numbers)

    print("Количество общих чисел:", count_common)


if __name__ == "__main__":
    main()
