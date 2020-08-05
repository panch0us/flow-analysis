import pandas

list_grz_1 = pandas.read_csv('C:/Users/asus/Desktop/home/test/potok/csv/номер/targets_05.08.2020 12_05_21.csv',
                             encoding='utf_16_le')
list_grz_2 = pandas.read_csv('C:/Users/asus/Desktop/home/test/potok/csv/номер/targets_05.08.2020 12_13_40.csv',
                             encoding='utf_16_le')

i = 0
z = 0
for grz_1 in list_grz_1['ГРЗ']:
    for grz_2 in list_grz_2['ГРЗ']:
        if grz_1 == grz_2:
            print('ГРЗ_1: ' + grz_1 + ' --- ГРЗ_2: ' + grz_2)

    i = i + 1
