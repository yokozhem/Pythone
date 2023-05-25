
# w - write
# r - read
# a - append
#fd - файл дескриптер 


# with open ('file.txt', 'w', encoding='utf-8') as fd:
#     fd.write('первая строка в этом файле')
# with open ('file.txt', 'a', encoding='utf-8') as fd:
#     fd.write('\nвторая строка в этом файле')
# with open ('file.txt', 'r', encoding='utf-8') as fd:
#     print(type(fd))
#     # z = fd.read()
#     z = fd.readlines()
#     for i in z:
#         print(i)

def add_contact(f):
    input_name = input('Введите Имя: ')
    input_last_name = input('Введите Фамилию: ')
    input_phone_number = input('Введите номер телефона: ')
    data = f'{input_last_name} ; {input_name} ; {input_phone_number}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Запись {data} добавлена')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_str = fd.readlines()
        return file_str


def print_all(f):
    adress_book = read_all(f)
    for line in adress_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)


def search_contacts(f):
    last_name = input('Введите Фамилию для поиска: ')
    adress_book = read_all(f)
    found_records = []
    for line in adress_book:
        if last_name in line:
            line = line.replace(';', '')
            line = line.replace('\n', '')
            found_records.append(line)
    if found_records:
        print(f'Найденные записи для фамилии {last_name}:')
        for record in found_records:
            print(record)
    else:
        print('Запись не найдена')


def modify_contact(f):
    last_name = input('Введите Фамилию для изменения: ')
    adress_book = read_all(f)
    found_indices = []
    for i, line in enumerate(adress_book):
        if last_name in line:
            found_indices.append(i)

    if found_indices:
        print(f'Найденные записи для фамилии {last_name}:')
        for i in found_indices:
            print(i, adress_book[i])

        idx = int(input('Введите индекс записи для изменения: '))
        if idx in found_indices:
            contact_parts = adress_book[idx].split(';')
            name = contact_parts[1].strip()
            phone_number = contact_parts[2].strip()

            print(f'Выбранная запись: {name} {last_name}, {phone_number}')

            field_choice = input('Выберите поле для изменения:\n'
                                 '1 - Имя\n'
                                 '2 - Фамилия\n'
                                 '3 - Номер телефона\n'
                                 'Выберите соответствующую цифру: ')

            if field_choice == '1':
                new_name = input('Введите новое имя: ')
                contact_parts[1] = new_name.strip()
            elif field_choice == '2':
                new_last_name = input('Введите новую фамилию: ')
                contact_parts[0] = new_last_name.strip()
            elif field_choice == '3':
                new_phone_number = input('Введите новый номер телефона: ')
                contact_parts[2] = new_phone_number.strip()
            else:
                print('Некорректный выбор поля.')

            new_record = ' ; '.join(contact_parts) + '\n'
            adress_book[idx] = new_record

            with open(f, 'w', encoding='utf-8') as fd:
                fd.writelines(adress_book)

            print('Запись успешно изменена.')
        else:
            print('Некорректный индекс.')
    else:
        print('Запись не найдена.')



def delete_contact(f):
    last_name = input('Введите Фамилию для удаления: ')
    adress_book = read_all(f)
    found_indices = []
    for i, line in enumerate(adress_book):
        if last_name in line:
            found_indices.append(i)

    if found_indices:
        print(f'Найденные записи для фамилии {last_name}:')
        for i in found_indices:
            print(i, adress_book[i])

        idx = int(input('Введите индекс записи для удаления: '))
        if idx in found_indices:
            del adress_book[idx]

            with open(f, 'w', encoding='utf-8') as fd:
                fd.writelines(adress_book)

            print('Запись успешно удалена.')
        else:
            print('Некорректный индекс')

def main():
    file = 'adress_book.txt'
    while True:
        user_choice = input(' 1 - добавить запись,\n 2 - прочитать всю тел. книгу,\n 3 - найти контакт,\n'
                            ' 4 - изменить контакт,\n 5 - удалить контакт,\n z - для выхода: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contacts(file)
        elif user_choice == '4':
            modify_contact(file)
        elif user_choice == '5':
            delete_contact(file)
        elif user_choice == 'z':
            print('Всего хорошего!')
            break


if __name__ == '__main__':
    main()

