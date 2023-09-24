def main():
    class Transport:

        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

        def seating_capacity(self, capacity):
            return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

    class Autobus(Transport):

        def __init__(self, name, max_speed, mileage):
            super().__init__(name, max_speed, mileage)

        def seating_capacity(self, capacity=50):
            return super().seating_capacity(capacity)

    autobus = Autobus('Renaul Logan', 180, 12)

    print(autobus.seating_capacity())


if __name__ == "__main__":
    main()
