def get_user_input(prompt):
    return input(prompt)

def main():
    animal = get_user_input("Введите вид питомца: ")
    animal_age = get_user_input("Введите возраст питомца: ")
    animal_name = get_user_input("Введите кличку питомца: ")

    output = f'Это {animal} по кличке "{animal_name}". Возраст: {animal_age} года.'
    print(output)

if __name__ == '__main__':
    main()
