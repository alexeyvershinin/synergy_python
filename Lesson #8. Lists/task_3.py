def main():
    m = int(input('ВВедите максимальную грузоподъемность лодки: '))
    n = int(input('Введите количество рыбаков: '))
    fishermens = []

    for i in range(n):
        weight = int(input(f'Введите вес рыбака № {i +1}: '))
        fishermens.append(weight)

    fishermens.sort()

    counter_boats = 0

    light = 0  # Индекс самого легкого рыбака
    heavy = n - 1  # Индекс самого тяжелого рыбака

    while light <= heavy:
        if fishermens[light] + fishermens[heavy] <= m:
            light += 1
            heavy -= 1
        else:
            heavy -= 1
        counter_boats += 1

    print(counter_boats)

if __name__ == "__main__":
    main()
