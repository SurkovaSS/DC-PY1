list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_el = list_numbers[0]
max_el_pos = 0
for pos, num in enumerate(list_numbers):
    if num > max_el:
        max_el = num
        max_el_pos = pos

list_numbers[max_el_pos] = list_numbers[-1]
list_numbers[-1] = max_el
print(list_numbers)
