def main():
    word = str(input("Введите слово латинскими буквами: "))
    letters = ['a', 'e', 'i', 'o', 'u']

    letter_counts = {}
    for letter in letters:
        letter_count = word.count(letter)
        if letter_count == 0:
            letter_count = False
        letter_counts[letter] = letter_count

    for key, value in letter_counts.items():
        print(key, value)

if __name__ == '__main__':
    main()

