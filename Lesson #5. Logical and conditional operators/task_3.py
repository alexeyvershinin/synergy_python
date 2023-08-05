def main():
    min_investment_amount = int(input("Введите минимальную сумму инвестиций: "))
    mike_cash = int(input("Введите количество денег которое хочет инвестировать Майк: "))
    ivan_cash = int(input("Введите количество денег которое хочет инвестировать Иван: "))

    total_cash = mike_cash + ivan_cash

    if min_investment_amount <= mike_cash and min_investment_amount <= ivan_cash:
        print(2)
    elif min_investment_amount <= mike_cash and min_investment_amount > ivan_cash:
        print('Mike')
    elif min_investment_amount <= ivan_cash and min_investment_amount > mike_cash:
        print('Ivan')
    elif min_investment_amount <= total_cash and min_investment_amount > ivan_cash and min_investment_amount > mike_cash:
        print(-1)
    else:
        print(0)


if __name__ == '__main__':
    main()
