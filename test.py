def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))


data = 'фио | номер телефона\n\
фио1 | номер телефона1\n\
Исаев Владислав Иванович | +814881481848\n\
Иванов Иван Иваныч | +16471845915'
print(data)
contact_to_find = input('Введите, что хотите найти: ')
print(search(data, contact_to_find))
