import pandas
# имортируем встроенный класс Counter из модуля collection, который подсчитывает количество вхождений
# элементов в списке. (Синтаксис: a = Counter(список); a.['нужный элемент списка для подсчета'])
from collections import Counter
"""
list_grz_1 = pandas.read_csv('C:/Users/asus/Desktop/home/test/potok/csv/номер/targets_05.08.2020 12_05_21.csv',
                             encoding='utf_16_le')
list_grz_2 = pandas.read_csv('C:/Users/asus/Desktop/home/test/potok/csv/номер/targets_05.08.2020 12_13_40.csv',
                             encoding='utf_16_le')

test_list_1 = []
for el in list_grz_1['ГРЗ']:
    test_list_1.append(el)

test_list_2 = []
for el in list_grz_2['ГРЗ']:
    test_list_2.append(el)


i = 0
# используем set (множество) для удаления повторяющихся элементов в списке
for grz_1 in set(test_list_1):
    if grz_1 in test_list_2:
        print(str(i) + ') ГРЗ_1: ' + grz_1 + ' -- количество этого ГРЗ во втором списке: ' + str(Counter(test_list_2)[grz_1]))
        i = i + 1
"""


def return_dict_all_grz():
    """Функция для приема любого количества списков ГРЗ, переработки их в нумерованный словарь,
    и возвращении полногго словаря с нумерованными списками ГРЗ"""
    stop = ''
    counter = 1
    list_input = []
    dict_input = {counter: list_input}
    while stop == '':
        list_input = []
        file = input('Введити название файла: ')
        #result = pandas.read_csv('C:/Users/umvd/Desktop/Анализ_потоков/csv/номер/' + file, encoding='utf_16_le')
        #result = pandas.read_csv('C:/Users/asus/Desktop/home/test/potok/csv/номер/' + file, encoding='utf_16_le')
        result = pandas.read_csv('C:/Users/panchous/Desktop/home/test/potok/csv/number/' + file, encoding='utf_16_le')
        for el in result['ГРЗ']:
            list_input.append(el)
            dict_input[counter] = list_input
        stop = input('Нажмите клавишу ENTER для продолжения.\nДля завершения введите любой символ и нажмите ENTER ')
        counter = counter + 1
    return dict_input

dict_input = return_dict_all_grz()

count_element_from_dict = len(dict_input)

i = 1
b = 2

while i < count_element_from_dict and b < (count_element_from_dict + 1):
     print('\nАнализ совпадений ГРЗ списка № ' + str(i) + ' со списком № ' + str(b))
     for el in set(dict_input[i]):
         if el in dict_input[b]:
             print('ГРЗ ' + str(el) + '\t из списка № ' + str(i) + '\t---> совпадение со списком № ' + str(b))
     b = b + 1

"""
     if count_element_from_dict > 2:
         i = i + 1
         b = b + 1
         print('Анализ совпадений ГРЗ списка № ' + str(i) + ' со списком № '
+ str(b))
         for el in set(dict_input[i]):
             if el in dict_input[b]:
                 print('ГРЗ ' + str(el) + '\t из списка № ' + str(i) +
'\t---> совпадение со списком № ' + str(b))
"""

