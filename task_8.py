# TODO Определить, сколько можно прожить, используя только подушку и зарплату.

def months_to_live(money_capital: int, salary: int, spend: int, increase: float) -> None:
    """
    :param money_capital: финансовая подушка безопасности
    :param salary: ежемесячная зарплата
    :param spend: расходы на проживание в месяц
    :param increase: рост цен ежемесячно
    :return: None
    """
    month = 0  # Первый месяц.

    total_money = money_capital + salary
    total_spend = 0

    while total_spend <= total_money:
        month += 1
        spend = spend + spend * increase
        total_spend = total_spend + spend

    print(month)


months_to_live(10000, 5000, 6000, 0.03)
