def write_to_file(persons: list, filename: str):
    """ Запись данных в файл """
    with open(filename, 'w', encoding='utf-8') as file:
        for person in persons:
            person_lst = person.split(' // ')
            file.write(' // '.join(person_lst))
    
def read_from_file(filename: str) -> list:
    """ Чтение данных из файла """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines
