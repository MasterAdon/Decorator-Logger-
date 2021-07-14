from logger import log_decoration, log_decoration1

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
@log_decoration
# @log_decoration1
def sort_name_docnumber(doc):
    ''' function for sorting a directory
     number document ->>> name user '''

    num_in = (input('Введите номер документа: '))
    need_name = str()
    for key in doc:
        if key["number"] == num_in:
            need_name += (key["name"])
    if need_name != str():
        print(need_name)
    else:
        print('Документ с таким номером отсутсвует в каталоге')

    return


# sort_name_docnumber(documents)
@log_decoration
# @log_decoration1
def searh_number_shelf(direct):
    ''' function for search shelf
    number document ->>> number shelf '''
    num_in = (input('Введите номер документа: '))
    num_shelf = str()
    for shelf, document in direct.items():  # видит все списки и полки, в том числе пустой список
        if num_in in document:
            num_shelf += shelf
    if num_shelf != str():
        print(f'Документ находится на полке № {num_shelf}')
    else:
        print('Документ с таким номером отсутсвует в каталоге')

    return


# searh_number_shelf(directories)
@log_decoration
# @log_decoration1
def output_document(doc):
    ''' function for document outpust '''
    for dic in doc:
        print(f'{dic["type"]}  "{dic["number"]}"  "{dic["name"]}"')

    return


# output_document(documents)


def new_document():
    ''' function for new document '''

    number_new = input('Введите номер документа: ')
    type_new = input('Введите тип документа: ')
    name_new = input('Введите имя обладателя документа: ')
    new_dict = {"type": type_new, "number": number_new, "name": name_new}
    documents.append(new_dict)
    num_shelf = (input('Введите номер полки для размещения документа: '))
    if num_shelf in directories.keys():
        directories[num_shelf].append(number_new)
        print('Документ добавлен')
    else:
        print('Полка с таким номером не используеться')

    return


# new_document()
# output_document(documents)
def main():
    while True:
        user_imp = (input("Введите команду действия (p,s,l,a,end): "))
        if user_imp == 'p':
            sort_name_docnumber(documents)
        elif user_imp == 's':
            searh_number_shelf(directories)
        elif user_imp == 'l':
            output_document(documents)
        elif user_imp == 'a':
            new_document()
        elif user_imp == 'end':
            print("Работа с программой завершена")
            break
        else:
            print('Неправильная команда')

# Функция для более удобного  тестирования декораторов
@log_decoration
# @log_decoration1
def tester(name):
    res = name * 7
    return res


if __name__ == '__main__':
    #main()
    tester(8)


