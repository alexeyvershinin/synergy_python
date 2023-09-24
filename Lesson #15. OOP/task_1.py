def main():
    class Transport:

        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

        def get_info_about_transport(self):
            return f'{self.name} Скорость: {self.max_speed} Пробег: {self.mileage}'

    autobus = Transport('Renaul Logan', 180, 12)

    print(autobus.get_info_about_transport())


if __name__ == "__main__":
    main()
