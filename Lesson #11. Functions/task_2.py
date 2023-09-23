import collections

pets = {}

def create():
    last_id = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last_id + 1


    pet_name = input("Имя питомца: ")
    pet_type = input("Вид питомца: ")
    pet_age = int(input("Возраст питомца: "))
    owner_name = input("Имя владельца: ")

    pets[new_id] = {
        pet_name: {
            "Вид питомца": pet_type,
            "Возраст питомца": pet_age,
            "Имя владельца": owner_name
        }
    }

def get_pet(ID):
    if ID in pets:
        return pets[ID]
    else:
        return False

def get_suffix(age):
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
    return age_string

def pets_list():
    for pet_id, pet_info in pets.items():
        for pet_name, details in pet_info.items():
            age = details["Возраст питомца"]
            age_suffix = get_suffix(age)
            print(f'Это {details["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {age} {age_suffix}. Имя владельца: {details["Имя владельца"]}')

def update(ID):
    if ID in pets:
        pet_info = pets[ID][list(pets[ID].keys())[0]]
        pet_info["Вид питомца"] = input("Новый вид питомца: ")
        pet_info["Возраст питомца"] = int(input("Новый возраст питомца: "))
        pet_info["Имя владельца"] = input("Новое имя владельца: ")
    else:
        print("Питомец с таким ID не найден.")

def delete(ID):
    if ID in pets:
        del pets[ID]
        print("Запись успешно удалена.")
    else:
        print("Питомец с таким ID не найден.")

def main():
    while True:
        print("\nВыберите операцию:")
        print("1. Создать запись о питомце")
        print("2. Прочитать информацию о питомце")
        print("3. Обновить информацию о питомце")
        print("4. Удалить запись о питомце")
        print("5. Вывести список всех питомцев")
        print("6. Выйти из программы")
        choice = input("Введите номер операции: ")

        if choice == '1':
            create()
        elif choice == '2':
            ID = int(input("Введите ID питомца: "))
            pet_info = get_pet(ID)
            if pet_info:
                for pet_name, details in pet_info.items():
                    age_suffix = get_suffix(details["Возраст питомца"])
                    print(f'Это {details["Вид питомца"]} по кличке "{pet_name}". Возраст питомца: {details["Возраст питомца"]} {age_suffix}. Имя владельца: {details["Имя владельца"]}')
            else:
                print("Питомец с таким ID не найден.")
        elif choice == '3':
            ID = int(input("Введите ID питомца для обновления: "))
            update(ID)
        elif choice == '4':
            ID = int(input("Введите ID питомца для удаления: "))
            delete(ID)
        elif choice == '5':
            pets_list()
        elif choice == '6':
            break
        else:
            print("Некорректная команда. Пожалуйста, выберите операцию из списка.")

if __name__ == "__main__":
    main()