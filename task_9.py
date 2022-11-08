# TODO Определить, какую нужно иметь сумму денег, чтобы прожить 10 месяцев, используя только эти деньги и зарплату.


def need_money_to_live(salary: int, spend: int, months: int, increase: float) -> None:
    """
    Функция выводит на экран сумму денег, чтобы прожить заданое количество месяцев с учетом повышения цен со
    второго месяца.

    :param salary: зарплата в месяц
    :param spend: траты в месяц
    :param months: количество месяцев, необходимых прожить
    :param increase: рост цен ежемесячно, начиная со второго месяца
    :return: None
    """
    total_spend = 0
    for month in range(1, months + 1):
        if month == 1:
            total_spend += spend
        else:
            spend = spend + spend * increase
            total_spend += spend

    need_money = total_spend - salary * months
    print(round(need_money))


need_money_to_live(5000, 6000, 10, 0.03)

