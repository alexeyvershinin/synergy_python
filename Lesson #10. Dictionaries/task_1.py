def main():
    pets = {}
    pets_number = int(input('Введите количество питомцев, которых хотите добавить в картотеку: '))

    pets_count = 1
    while pets_count <= pets_number:
        pet_info = {}

        print(f'Заполните информацию о питомце № {pets_count}')

        pet_name = input('Имя питомца: ')
        pet_type = input('Вид питомца: ')
        pet_age = int(input('Возраст питомца: '))
        owner_name = input('Имя владельца: ')

        pet_info['Вид питомца'] = pet_type
        pet_info['Возраст питомца'] = pet_age
        pet_info['Имя владельца'] = owner_name

        pets[pet_name] = pet_info
        pets_count += 1

    if len(pets) > 0:
        for pet_name, pet_info in pets.items():
            age = pet_info['Возраст питомца']
            last_digit = age % 10

            if 10 < age < 20:
                age_string = 'лет'
            else:
                if last_digit == 1:
                    age_string = 'год'
                elif 1 < last_digit < 5:
                    age_string = 'года'
                else:
                    age_string = 'лет'

            print(f'Это {pet_type} по кличке "{pet_name}". Возраст питомца: {age} {age_string}. Имя владельца: {owner_name}')


if __name__ == '__main__':
    main()
