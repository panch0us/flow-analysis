import pandas
from collections import Counter

list_grz_1 = pandas.read_csv('C:/Users/asus/Desktop/home/test/potok/csv/номер/targets_05.08.2020 12_05_21.csv',
                             encoding='utf_16_le')
list_grz_2 = pandas.read_csv('C:/Users/asus/Desktop/home/test/potok/csv/номер/targets_05.08.2020 12_13_40.csv',
                             encoding='utf_16_le')
print(type(list_grz_2))

test_list_1 = []
for el in list_grz_1['ГРЗ']:
    test_list_1.append(el)

test_list_2 = []
for el in list_grz_2['ГРЗ']:
    test_list_2.append(el)

result_counter_1 = Counter(test_list_1)
result_counter_2 = Counter(test_list_2)

print(result_counter_1['н408кр32'])


for grz_1 in test_list_1:
    if grz_1 in test_list_2:
        print('ГРЗ_1: ' + grz_1 + ' -- количество этого ГРЗ во втором списке: ' + str(Counter(test_list_2)[grz_1]))