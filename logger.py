from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные \n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address} \n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))

    while var != 1 and var !=2:
        print("Неправильный вод")
        var = int(input("Введите число: "))

    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address} \n\n")
    elif var == 2:
        with open("data_second_variant.csv", "a", encoding="utf-8") as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open("data_first_variant.csv", "r", encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) - 1:
                data_first_list.append("".join(data_first[j:i+1]))
                j = i
        print("".join(data_first_list))

    print("Вывожу данные из 2 файла: \n")
    with open("data_second_variant.csv", "r", encoding="utf-8") as f:
        data_second = f.readlines()
        print(*data_second)


def remove_contact():
    X = input('Введите Имя или Фамилию для удаления: ')
    variant = None
    with open("data_first_variant.csv", 'r', encoding="utf-8") as open_book:
        lines = open_book.readlines()

    with open("data_first_variant.csv", 'w', encoding="utf-8") as open_book:
        for line in lines:
            if X in line:
                variant = "data_first_variant"
            else:
                open_book.write(line)

    if variant == "data_first_variant":
        print(f"Контакт с именем/фамилией '{X}' удален из data_first_variant.csv.")
        return

    with open("data_second_variant.csv", 'r', encoding="utf-8") as open_book:
        lines = open_book.readlines()

    with open("data_second_variant.csv", 'w', encoding="utf-8") as open_book:
        for line in lines:
            if X in line:
                variant = "data_second_variant"
            else:
                open_book.write(line)

    if variant == "data_second_variant":
        print(f"Контакт с именем/фамилией '{X}' удален из data_second_variant.csv.")
    else:
        print(f"Контакт с именем/фамилией '{X}' не найден.")



def edit_contact():
    search_param = input('Введите параметр для редактирования: ').lower()
    add_i = input('Введите новое имя: ').title()
    add_f = input('Введите новую фамилию: ').title()
    add_tel = input('Введите новый телефон: ').title()
    add_adr = input('Введите новый адрес: ').title()
    
    updated_line_1 = f"{add_i}\n{add_f}\n{add_tel}\n{add_adr}\n"
    updated_line_2 = f"{add_i};{add_f};{add_tel};{add_adr}\n"
    
    with open("data_first_variant.csv", 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open("data_first_variant.csv", 'w', encoding='utf-8') as file:
        for i, line in enumerate(lines):
            if search_param in line.lower() and i % 4 == 0:
                lines[i] = f"{add_i}\n"
                print(f"Имя контакта с параметром '{search_param}' было изменено на '{add_i}'.")
            elif search_param in line.lower() and i % 4 == 1:
                lines[i] = f"{add_f}\n"
                print(f"Фамилия контакта с параметром '{search_param}' была изменена на '{add_f}'.")
            file.write(lines[i])
        file.write('\n')

    with open("data_second_variant.csv", 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open("data_second_variant.csv", 'w', encoding='utf-8') as file:
        for line in lines:
            if search_param in line.lower():
                file.write(updated_line_2)
                print(f"Контакт с параметром '{search_param}' отредактирован.")
            else:
                file.write(line)
        file.write('\n')




