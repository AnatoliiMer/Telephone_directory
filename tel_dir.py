def import_data(file_name): #функции импорта данных из текстового файла
    entries = []
    with open(file_name, 'r') as file:
        for line in file:
            entry = line.strip().split()
            entries.append(entry)
    return entries


def export_data(file_name, entries): #функция записи введенных данных в текстовый файл
    with open(file_name, 'w') as file:
        for entry in entries:
            file.write(' '.join(entry) + '\n')



def copy_data(file_name, target_file): #функция экспорта данных в новый файл
    with open(file_name, 'r') as source:
        with open(target_file, 'w') as target:
            for line in source:
                target.write(line)



def print_data(entries): #функция вывода данных 
    if len(entries) > 0:
        print('Фамилия  Имя      Отчество Номер телефона')
        print('------------------------------------------')
        for entry in entries:
            print(f'{entry[0]:<8} {entry[1]:<8} {entry[2]:<8} {entry[3]}')
    else:
        print('Нет данных для вывода')


def search_data(entries, search_string): #функция поиска записей по заданному критерию
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
            target_file = input("Введите название нового файла: ")
            copy_data(file_name, target_file + '.txt')
            print(f'Данные экспортированы в файл c названием - {target_file}.txt')
            
        elif choice == '5':
            break
        else:
            print('Неверный выбор')

if __name__ == '__main__':
    main()

