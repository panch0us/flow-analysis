import pandas
# имортируем встроенный класс Counter из модуля collection, который подсчитывает количество вхождений
# элементов в списке. (Синтаксис: a = Counter(список); a.['нужный элемент списка для подсчета'])
#from collections import Counter


def return_dict_all_grz():
    """Функция принимает любого количество файлов с ГРЗ формата CSV для переработки их в нумерованный словарь,
    и возвращает полный словарь с нумерованными списками ГРЗ"""
    stop = ''
    counter = 1
    list_input = []
    dict_input = {counter: list_input}
    while stop == '':
        list_input = []
        file = input('Введити название файла: ')
        result = pandas.read_csv('C:/Users/umvd/Desktop/Анализ_потоков/csv/номер/' + file, encoding='utf_16_le')
        # result = pandas.read_csv('C:/Users/asus/Desktop/home/test/potok/csv/номер/' + file, encoding='utf_16_le')
        # result = pandas.read_csv('C:/Users/panchous/Desktop/home/test/potok/csv/number/' + file, encoding='utf_16_le')
        for el in result['ГРЗ']:
            list_input.append(el)
            dict_input[counter] = list_input
        stop = input('[enter] - ПРОДОЛЖЕНИЕ\n[символ + enter] - ЗАВЕРШЕНИЕ')
        counter = counter + 1
    return dict_input


def iteration_one_to_many_lists(func_return_dict_all_grz):
    """Функция получает словарь, состоящий из {номера списка: списка ГРЗ} из функции return_dict_all_grz.
    После проводит итерацию по каждому полученному списку ГРЗ, сравнивая каждый номер первого списка со следующим
    по порядку списком."""
    # Получаем словарь вида {№: '[список ГРЗ]} из ввоада пользователя
    dict_input = func_return_dict_all_grz()
    # Считаем количество списков в ГРЗ в полученом словаре
    count_element_from_dict = len(dict_input)
    i = 0
    b = 1
    # Выполняем цикл по количеству списков ГРЗ в словаре
    while i < count_element_from_dict:
        i = i + 1
        b = b + 1
        while b < (count_element_from_dict + 1):
            print('\n----Анализ совпадений ГРЗ списка № ' + str(i) + ' со списком № ' + str(b) + '----')
            # Применяем set(множество) к списку ГРЗ для удаления повторяющихся ГРЗ.
            for el in set(dict_input[i]):
                if el in dict_input[b]:
                    print(str(el) + '\t из списка № ' + str(i) + '\t---> совпадение со списком № ' + str(b))
            b = b + 1
        b = 1 + i


iteration_one_to_many_lists(return_dict_all_grz)
