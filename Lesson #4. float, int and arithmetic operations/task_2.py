def power_of_tens_to_units(number):
    number_str = str(number)

    try:
        if len(number_str) != 5:
            raise Exception("В числе должно быть 5 знаков.")

        number_str_array = []
        for symbol in number_str:
            number_str_array.append(int(symbol))

        a = number_str_array
        return a[3] ** a[4] * a[2] / (a[0] - a[1])


    except Exception as e:
        print(e)


def main():
    number = 46275
    result = power_of_tens_to_units(number)
    print(result)


if __name__ == '__main__':
    main()
