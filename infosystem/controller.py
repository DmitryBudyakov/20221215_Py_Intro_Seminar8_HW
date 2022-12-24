import model
import view
import logger

def run():
    while True:
        view.cls_show_app_head()
        selector = view.show_top_menu(top_menu, top_menu_choice, top_menu_actions)
        if selector == '1':   # добавление сотрудника
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_add_person)
            print(msg_existing_persons)
            view.show_person_head(person_head)
            all_persons = logger.read_from_file(infosys_db_file)
            model.printout_persons(all_persons)
            print()
            added_person = view.update_person()
            updated_persons = model.add_new_person(all_persons, added_person)
            sorted_list = model.sort_persons(updated_persons)
            logger.write_to_file(sorted_list, infosys_db_file)
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_add_person)
            print(msg_after_add)
            view.show_person_head(person_head)
            model.printout_persons(sorted_list)
            print()
            input(msg_back_top_menu)
        elif selector == '2':     # поиск сотрудника
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_search_person)
            searched_person = view.search_person()
            print('Найденные сотрудники:')
            view.show_person_head(person_head)
            all_persons = logger.read_from_file(infosys_db_file)
            model.print_found_person(all_persons, searched_person)
            print()
            input(msg_back_top_menu)
        elif selector == '3':   # удаление сотрудника
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_del_person)
            print(msg_existing_persons)
            view.show_person_head(person_head)
            all_persons = logger.read_from_file(infosys_db_file)
            model.printout_persons(all_persons)
            print()
            person_to_del = view.get_person_num(msg_to_delete)
            persons_after_del = model.delete_person(all_persons, person_to_del)
            logger.write_to_file(persons_after_del, infosys_db_file)
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_del_person)
            print(msg_after_del)
            view.show_person_head(person_head)
            model.printout_persons(persons_after_del)
            print()
            input(msg_back_top_menu)
        elif selector == '4':   # изменение сотрудника
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_modify_person)
            view.show_person_head(person_head)
            all_persons = logger.read_from_file(infosys_db_file)
            model.printout_persons(all_persons)
            print()
            person_num_to_modify = view.get_person_num(msg_to_modify)
            modified_person = view.update_person()
            modified_persons_sorted = model.sort_persons(model.modify_person(all_persons, modified_person, person_num_to_modify))
            logger.write_to_file(modified_persons_sorted, infosys_db_file)
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_modify_person)
            print(msg_after_modify)
            view.show_person_head(person_head)
            model.printout_persons(modified_persons_sorted)
            print()
            input(msg_back_top_menu)
        elif selector == '5':   # вывод всех сотрудников
            view.cls_show_app_head()
            view.show_sub_menu(sub_menu_show_persons)
            print(msg_existing_persons)
            view.show_person_head(person_head)
            all_persons = logger.read_from_file(infosys_db_file)
            model.printout_persons(all_persons)
            print()
            input(msg_back_top_menu)


global msg_back_top_menu

infosys_db_file = 'infosystem/db.csv'

msg_back_top_menu = 'Нажмите [Enter] чтобы вернуться в Главное меню: '
msg_to_delete = 'Введите номер (No.) удаляемого сотрудника: '
msg_to_modify = 'Введите номер (No.) изменяемого сотрудника: '
msg_existing_persons = 'Список существующих сотрудников:\n'
msg_after_del = 'Список сотрудников после удаления:\n'
msg_after_modify = 'Список сотрудников после изменения:\n'
msg_after_add = 'Список сотрудников после добавления:\n'

# app_title = 'Информационная система АО "Маугли и сыновья"'
sub_menu_add_person = '1. Добавить сотрудника\n'
sub_menu_search_person = '2. Найти сотрудника\n'
sub_menu_del_person = '3. Удалить сотрудника\n'
sub_menu_modify_person = '4. Изменить данные сотрудника\n'
sub_menu_show_persons = '5. Показать список всех сотрудников\n'
menu_item_exit = 'q. Выйти\n'
top_menu = 'Главное меню:\n'\
    + sub_menu_add_person\
    + sub_menu_search_person\
    + sub_menu_del_person\
    + sub_menu_modify_person\
    + sub_menu_show_persons\
    + menu_item_exit
top_menu_choice = "Выбрать действие [1-5,q]: "
top_menu_actions = ['1','2','3','4','5','q']

person_head = \
"No. // Id // ФАМИЛИЯ // ИМЯ // ТЕЛЕФОН // ДОЛЖНОСТЬ // e-mail"
# ---\t---\t-------\t---\t-------\t---------\t------"
