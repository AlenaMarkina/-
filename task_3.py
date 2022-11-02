# TODO продолжить заполнение словаря
dict_hex = {
    '0x0': 0,
    '0x1': 1,
    '0x2': 2,
}

for i in range(3, 16):
    if i in range(10, 16):
        old_str = hex(i)
        small_last_letter = old_str[-1]
        capital_last_letter = small_last_letter.capitalize()
        new_str = old_str.replace(small_last_letter, capital_last_letter)
        dict_hex.update({new_str: i})
    else:
        dict_hex.update({hex(i): i})

print(dict_hex)