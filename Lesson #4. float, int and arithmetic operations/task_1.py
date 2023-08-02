def main():
    a, b = input('Введите длину сторон прямоугольника через пробел: ').split()
    a = int(a) if a.isdecimal() else float(a)
    b = int(b) if b.isdecimal() else float(b)
    print('Периметр прямоугольника', 2 * a + 2 * b, sep='=')
    print('Площадь прямоугольника', round(a * b, 3), sep='=')


if __name__ == '__main__':
    main()
