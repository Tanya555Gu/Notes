import csv


def readfile(filename):
    read_data = []
    with open('notes.txt', 'r', encoding='utf-8') as file:
        for elem in file:
            read_data.append(elem.split())
    return read_data


def menu():
    print('==============================')
    print('Выберите интересующий пункт')
    print('1: Вывести все заметки на экран')
    print('2: Поиск заметки')
    print('3: Добавдение заметки')
    print('4: Изменение заметки')
    print('5: Удаление заметки')
    print('6: Выход из программы')


def printinfo(data):
    print('Номер \t Краткое содержание \t Заметка')
    for elem in data:
        print(*elem, sep='\t')


def search(data):
    what = input('Что ищем? ')
    searched_data = []
    for string in data:
        for elem in string:
            if (what in elem) and string not in searched_data:
                searched_data.append(string)
    if searched_data:
        printinfo(searched_data)
    else:
        print('Строки, удовлетворяющие условиям поиска, не найдены')


def delete(data):
    id = input('Введите номер заметки для удаления: ')
    new_data = []
    for elem in data:
        if elem[0] != id:
            new_data.append(elem)
    return new_data


def add_note(data):
    id = input('Введите номер новой заметки: ')
    summary_note = input('Введите краткое содержание новой заметки: ')
    note = input('Введите текст новой заметки: ')
    data.append((id, summary_note, note))
    return data


def change_note():
    pass


def save(data):
    with open('notes.txt', 'w', encoding='utf-8') as file:
        for elem in data:
            stroka = ';'.join(elem) + '\n'
            file.write(stroka)


def main():
    my_choice = -1
    changed = False
    # словарь номеров команд и привязанных к ним функций
    operations = {
        1: printinfo,
        2: search,
        3: add_note,
        4: change_note,
        5: delete        
    }
    data = readfile('tel.txt')
    while my_choice != 6:
        menu()
        my_choice = int(input('Введите команду: '))
        if 1 <= my_choice <= 2:
            operations[my_choice](data)
        elif 3 <= my_choice <= 5:
            changed = True
            data = operations[my_choice](data)
        elif my_choice == 6:
            if changed:
                print('Данные были изменены. Идет сохранение данных')
                save(data)
            print('До свидания')
        else:
            print('Введена неправильная команда')


if __name__ == '__main__':
    main()