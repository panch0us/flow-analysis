import pandas
# имортируем встроенный класс Counter из модуля collection, который подсчитывает количество вхождений
# элементов в списке. (Синтаксис: a = Counter(список); a.['нужный элемент списка для подсчета'])
from collections import Counter

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