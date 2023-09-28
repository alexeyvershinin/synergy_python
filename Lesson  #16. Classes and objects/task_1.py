def main():
    class CashRegister:
        def __init__(self):
            self.balance = 0

        def top_up(self, amount):
            if amount > 0:
                self.balance += amount
            else:
                raise ValueError('Вы не можете внести в кассу отрицательное число денег')

        def count_1000(self):
            result = self.balance // 1000
            return f'В кассе нет тысяч' if result < 1 else f'Тысяч в кассе: {result}'

        def take_away(self, amount):
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError('Недостаточно средств в кассе для снятия')

        def get_balance(self):
            return f'Баланс кассы: {self.balance}'

    box_office = CashRegister()

    box_office.top_up(3500)

    print(box_office.get_balance())
    print(box_office.count_1000())
    print(box_office.take_away(4000))


if __name__ == "__main__":
    main()