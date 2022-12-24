def printout_persons(lines: list):
    line_num = 0
    for line in lines:
        line_num += 1
        pers_num = f'{line_num}. // '
        print(pers_num + line[:-1])

def print_found_person(persons: list, to_find: str):
    count = 0
    for entry in persons:
        if to_find.lower() in entry.lower():
            count += 1
            pers_num = f'{count}. // '
            print(pers_num + entry[:-1])
    if count == 0:
        print(f"Сотрудники по фильтру '{to_find}' не найдены.")

def add_new_person(persons: list, person: list) -> list:
    """ Добавление сотрудника к списку сотрудников """
    new_person = f"{' // '.join(person)}\n"
    persons.append(new_person)
    return persons

def modify_person(persons: list, person: list, person_num: int) -> list:
    """ Изменение данных сотрудника """
    upd_person = f"{' // '.join(person)}\n"
    persons[person_num - 1] = upd_person
    return persons

def sort_persons(pesrons: list) -> list:
    """ Сортировка списка сотрудников """
    sorted_list = sorted(pesrons)
    return sorted_list

def delete_person(persons: list, person_num: int) -> list:
    """ Удаление сотрудника по его No. в списке """
    del(persons[person_num-1])
    return persons
