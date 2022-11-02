BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 100  # TODO ввести количество страниц в книге
lines = 50  # TODO ввести количество строк на странице
chars = 25  # TODO ввести количество символов в строке

total_chars = pages * lines * chars  # TODO общее количество символов в книге
total_bytes = total_chars * BYTES_ONE_CHAR  # TODO размер одной книги в байтах  125000

bait_in_kilobait = 1024
kilobait_in_megabait = 1024
disk_value_in_megabait = 1.44  # размер дискеты в мега байтах

disk_size = disk_value_in_megabait * bait_in_kilobait * kilobait_in_megabait  # TODO размер дискеты в байтах

print(float(int(disk_size / total_bytes)))  # TODO найти количество книг, которое поместится на дискете
