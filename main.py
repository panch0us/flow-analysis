import pandas
# импортируем openpyxl для работы с таблицами xlsx
import openpyxl
# имортируем встроенный класс Counter из модуля collection, который подсчитывает количество вхождений
# элементов в списке. (Синтаксис: a = Counter(список); a.['нужный элемент списка для подсчета'])
#from collections import Counter

# указываем дирректорию расположения файлов для дальнейшей обработки
#DIRECTORY = 'C:/Users/asus/Desktop/home/test/analiz/csv/number/'
DIRECTORY = 'C:/Users/umvd/Desktop/Анализ_потоков/csv/номер/'

def return_dict_all_grz():
    """Функция принимает любого количество файлов с ГРЗ формата CSV для переработки их в нумерованный словарь,
    и возвращает полный словарь с нумерованными списками ГРЗ"""
    stop = ''
    counter = 1
    list_input = []
    dict_input = {counter: list_input}
    other_grz = []
    while stop == '':
        list_input = []
        file = input('Введити название файла: ')
        try:
            # result = pandas.read_csv(DIRECTORY + file, encoding='utf_16_le')
            result = pandas.read_csv(DIRECTORY + file, encoding='utf_16_le')
            # result = pandas.read_csv(DIRECTORY + file, encoding='utf_16_le')
            for el in result['ГРЗ']:
                list_input.append(el)
                dict_input[counter] = list_input
                if str(el[-2:]) != str(32):
                    other_grz.append(el)
            stop = input('ПРОДОЛЖЕНИЕ [enter]\nЗАВЕРШЕНИЕ [символ + enter]')
            counter = counter + 1
        except FileNotFoundError:
            print('Файл \'' + str(file) + '\' отсутвует в дирректории C:/Users/umvd/Desktop/Анализ_потоков/csv/номер/')
            continue
        except PermissionError:
            print('Ошибка: "PermissionError", попробуйте снова')
            continue
    return dict_input, other_grz


def iteration_one_to_many_lists(dict_input_user):
    """Функция получает словарь, состоящий из {номера списка: списка ГРЗ} из функции return_dict_all_grz.
    После проводит итерацию по каждому полученному списку ГРЗ, сравнивая каждый номер первого списка со следующим
    по порядку списком."""
    # Получаем словарь вида {№: '[список ГРЗ]} из ввоада пользователя
    dict_input = dict_input_user
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
    return dict_input


def iteration_summ_list(dict_input_user):
    """Добавить описание"""
    a = 1
    b = 2
    i = 0
    dict_input = dict_input_user
    while a < len(dict_input):
        print('------ СОВПАДЕНИЯ СПИСКА № ' + str(a) + ' -------')
        while i < len(dict_input) and b < (len(dict_input) + 1):
            if len(set(dict_input[a]) & set(dict_input[b])) > 0:
                print('Совпадения между списком № ' + str(a) + ' и списком № ' + str(b))
                print(set(dict_input[a]) & set(dict_input[b]))
                result = list(set(dict_input[a]) & set(dict_input[b]))
                b = b + 1
                while i < len(dict_input) and b < (len(dict_input) + 1):
                    if len(set(result) & set(dict_input[b])) > 0:
                        print('Совпадения предыдущих списков со списокм № ' + str(b))
                        print(set(result) & set(dict_input[b]))
                        result = list(set(result) & set(dict_input[b]))
                        b = b + 1
                    else:
                        print('Нет совпадений предыдущих списков со списокм № ' + str(b))
                        b = b + 1
                    i = i + 1
            else:
                print('Совпадения между списком № ' + str(a) + ' и списком № ' + str(b) + ' НЕТ')
                b = b + 1
        a = a + 1
        b = a + 1


dict_input, other = return_dict_all_grz()


first = iteration_one_to_many_lists(dict_input)
iteration_summ_list(dict_input)

print('Список номеров из других регионов, а также с нечитаемым регионом')
print(other)
