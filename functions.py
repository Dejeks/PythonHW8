def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def edit_data() -> None:
    """Изменяет данные в справочнике."""
    data = read_data()
    if data:
        print('Выберите запись для изменения:')
        print_data(data)
        index = int(input('Введите номер записи: '))
        if index >= 1 and index <= len(data):
            new_fio = input('Введите новое ФИО: ')
            new_phone_num = input('Введите новый номер телефона: ')
            data[index - 1] = f'{new_fio} | {new_phone_num}'
            write_data(data)
            print('Запись успешно изменена.')
        else:
            print('Некорректный номер записи.')
    else:
        print('Справочник пуст.')


def delete_data() -> None:
    """Удаляет данные из справочника."""
    data = read_data()
    if data:
        print('Выберите запись для удаления:')
        print_data(data)
        index = int(input('Введите номер записи: '))
        if index >= 1 and index <= len(data):
            del data[index - 1]
            write_data(data)
            print('Запись успешно удалена.')
        else:
            print('Некорректный номер записи.')
    else:
        print('Справочник пуст.')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    data = read_data()
    if data:
        contact_to_find = input('Введите, что хотите найти: ')
        result = search(data, contact_to_find)
        if result:
            print_data(result)
        else:
            print('Записи не найдены.')
    else:
        print('Справочник пуст.')


def read_data() -> list[str]:
    """Читает данные из справочника и возвращает список записей."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().splitlines()
    return data


def write_data(data: list[str]) -> None:
    """Записывает данные в справочник."""
    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


def print_data(data: list[str]) -> None:
    """Выводит данные справочника на экран."""
    for i, contact in enumerate(data, start=1):
        print(f'{i}. {contact}')


def search(data: list[str], info: str) -> list[str]:
    """Находит записи по определенному критерию поиска"""
    return [contact for contact in data if info.lower() in contact.lower()]