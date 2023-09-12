def main():
    s = input('Введите строку без пробелов: ')
    if s == s[::-1]:
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    main()
