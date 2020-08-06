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
        result = pandas.read_csv('C:/Users/asus/Desktop/home/test/potok/csv/номер/' + file, encoding='utf_16_le')
        for el in result['ГРЗ']:
            list_input.append(el)
            dict_input[counter] = list(list_input)
        stop = input('Введите любой символ для завершения добавления файлов: ')
        #print(dict_input[counter])
        counter = counter + 1
    return dict_input

dict_input = return_dict_all_grz()

count_key_from_dict = int(len(dict_input))
print(count_key_from_dict)

list_grz = []
for key, value in dict_input.items():
    print(key, value)
    print(type(dict_input.items()))

"""
x = 0
for key, value in dict_input.items():
    count = Counter(value)
    for el in count:
        print(count[el])
"""


