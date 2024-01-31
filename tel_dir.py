def import_data(file_name):
    entries = []
    with open(file_name, 'r') as file:
        for line in file:
            entry = line.strip().split()
            entries.append(entry)
    return entries





def export_data(file_name, target_file):
    with open(file_name, 'r') as source:
        with open(target_file, 'w') as target:
            for line in source:
                target.write(line)




def print_data(entries):
    if len(entries) > 0:
        print('Фамилия  Имя      Отчество Номер телефона')
        print('------------------------------------------')
        for entry in entries:
            print(f'{entry[0]:<8} {entry[1]:<8} {entry[2]:<8} {entry[3]}')
    else:
        print('Нет данных для вывода')


def search_data(entries, search_string):
    results = []
    for entry in entries:
        if search_string.lower() in ' '.join(entry).lower():
            results.append(entry)
    return results


def main():
    file_name = 'phonebook.txt'
    entries = import_data(file_name)

    while True:
        print('\nТелефонный справочник')
        print('1. Вывести все записи')
        print('2. Добавить новую запись')
        print('3. Найти записи')
        print('4. Экспортировать данные')
        print('5. Выход')

        choice = input('Выберите действие: ')

        if choice == '1':
            print_data(entries)
        elif choice == '2':
            last_name = input('Введите фамилию: ')
            first_name = input('Введите имя: ')
            middle_name = input('Введите отчество: ')
            phone_number = input('Введите номер телефона: ')
            entry = [last_name, first_name, middle_name, phone_number]
            entries.append(entry)
            export_data(file_name, entries)
            print(f'Данные записаны в справочник {file_name}')
        elif choice == '3':
            search_string = input('Введите строку поиска: ')
            results = search_data(entries, search_string)
            print_data(results)
        elif choice == '4':
            target_file = input("Введите название файла-приемника: ")
            export_data(file_name, target_file)
            print(f'Данные экспортированы в файл {target_file}')
            #export_data(file_name, entries)
            #print(f'Данные экспортированы в файл {file_name}')
        elif choice == '5':
            break
        else:
            print('Неверный выбор')

if __name__ == '__main__':
    main()

