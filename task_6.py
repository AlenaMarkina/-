list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Поменять местами первый максимальный и последний элементы.

max_element = 0
index_of_max_element = 0

for i in range(len(list_numbers)):
    if list_numbers[i] > max_element:
        max_element = list_numbers[i]
        index_of_max_element = i

list_numbers[index_of_max_element], list_numbers[-1] = list_numbers[-1], list_numbers[index_of_max_element]

print(list_numbers)
