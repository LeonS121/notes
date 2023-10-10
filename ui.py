import Note


def create_note(number):
    title = check_len_text_input(
        input('Название заметки: '), number)
    body = check_len_text_input(
        input('Описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nВ этой программе имеются следующие функции:\n\n1 - все заметки \n2 - новая заметка\n3 - удаление заметки\n4 - редактирование заметки\n5 - поиск заметок по дате\n6 - поиск заметок по id\n7 - выход\n\nВведите интересующую вас функцию: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Спасибо что выбрали нас :)")
