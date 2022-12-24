import os

def clear_screen():
    """ очистка экрана """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def app_head():
    """ Заголовок программы """
    title = 'Информационная система АО "Маугли и сыновья"'
    title_line = '-'*len(title)
    head = f'{title_line}\n{title}\n{title_line}'
    print(head)

def cls_show_app_head():
    """ Очистка экрана и вывод заголовка """
    clear_screen()
    app_head()

def show_top_menu(menu_top_head: str, menu_top_choice: str, actions: list) -> str:
    """ Главное меню """
    top_menu = menu_top_head + menu_top_choice
    while True:
        action = input(top_menu)
        if action not in actions:
            top_menu = menu_top_head + error_msg_select + menu_top_choice
            cls_show_app_head()
        elif action == 'q':
            print(msg_on_exit)
            exit()
        else:
            return action
        
def show_sub_menu(title: str):
    """ Показывает подменю """
    menu_title = f'Меню:\n{title}'
    cls_show_app_head()
    print(menu_title)
    
def search_person() -> str:
    """ Запрос на поиск """
    search_string = input('Введите данные для поиска: ')
    return search_string
    
def show_person_head(person_head: str):
    """ Поля справочника """
    print(person_head)

def update_person() -> list:
    """ Добавление/Изменение данных сотрудника
        Возвращает список с данными добавляемого/изменяемого сотрудника
    """
    person_upd = []
    person_id = input('Id\t\t: ')
    family_name = input('Фамилия\t\t: ')
    first_name = input('Имя\t\t: ')
    phone_number = input('Номер телефона\t: ')
    position = input('Должность\t: ')
    email = input('e-mail\t\t: ')
    person_upd.append(person_id)
    person_upd.append(family_name)
    person_upd.append(first_name)
    person_upd.append(phone_number)
    person_upd.append(position)
    person_upd.append(email)
    return person_upd

def get_person_num(prompt: str) -> int:
    """ Возвращает No. сотрудника из списка """
    pers_number = int(input(prompt))
    return pers_number

global msg_on_exit, error_msg       
msg_on_exit = '\nВыход из системы. Пока!\n'
error_msg_select = 'Ошибка ввода. Повторите ввод.\n'
