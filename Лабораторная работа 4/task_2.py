# Данная функция выдвет "корректный" ответ
def get_count_char(str_):
    dictionary = dict()
    to_check = str_.lower().replace(' ', '')  # TODO посчитать количество каждой буквы в строке в аргументе str_

    for char in to_check:
        if char.isalpha():
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
    return dictionary

#Данная функция написана по рекомендациям , main_str
# def get_count_char(str_):
#     dictionary = dict()
#     to_check = str_.lower().split()  # TODO посчитать количество каждой буквы в строке в аргументе str_
#     to_check.sort()
#     stroka = str(to_check)
#     for char in stroka:
#         if char.isalpha():
#             if char in dictionary:
#                 dictionary[char] += 1
#             else:
#                 dictionary[char] = 1
#     return dictionary

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def get_percent_char(dict_):

    all = sum(dict_.values())
    for key, value in dict_.items():
        dict_[key] = value/all
    return dict_

#print(get_percent_char(get_count_char(main_str)))