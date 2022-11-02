# TODO найти сумму, количество и среднее арифметическое уникальных чисел

list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

list_of_unique_numbers = set(list_)

sum_of_unique_numbers = sum(list_of_unique_numbers)
amount_of_unique_numbers = len(list_of_unique_numbers)
arithmetic_mean = round((sum_of_unique_numbers / amount_of_unique_numbers), 5)

print(sum_of_unique_numbers)
print(amount_of_unique_numbers)
print(arithmetic_mean)
