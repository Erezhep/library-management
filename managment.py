import os
from books import Book
from storage import LibraryStorage

def add_book():
    """
    Добавляет новую книгу в библиотеку, запрашивая данные у пользователя.
    Запрашивает название, автора и год издания книги.
    В случае неправильного ввода года допускает три попытки, после чего завершает выполнение.

    Исключения:
        ValueError: Если пользователь ввел некорректный год.
        Exception: Любая другая ошибка ввода.
    """
    print("Чтобы добавить, введите данные о книге!")
    title = input("Введите названия книг: ")
    author = input("Введите автор: ")
    again_count = 0
    while True:
        if again_count > 3:
            clear_console()
            print("У вас было три попытка. Начинайте все с начала в целях безопасности")
            break
        try:
            year = int(input("Введите год издания книг: "))
            break
        except ValueError as e:
            print("Введите число")
            again_count += 1
            continue
        except Exception as e:
            print("Введите то, что нужно ввести")
            again_count += 1
            continue
    if again_count > 3:
        return
    else:
        LibraryStorage.add_book(title, author, year)

def delete_book():
    """
    Удаляет книгу из библиотеки по её ID, запрашивая ID у пользователя.
    Допускает три попытки ввода правильного ID, после чего завершает выполнение.

    Исключения:
        ValueError: Если пользователь ввел некорректный ID.
        Exception: Любая другая ошибка ввода.
    """
    again_count = 0
    while True:
        if again_count > 3:
            clear_console()
            print("У вас было три попытка. Начинайте все с начала в целях безопасности")
            break
        try:
            id = int(input("Введите ID книги, которую нужно удалить: "))
            if id <= 0:
                print("ID должен быть положительным числом")
                again_count += 1
                continue
            else:
                LibraryStorage.delete_book(id)
                break
        except ValueError:
            print("Введите число")
            again_count += 1
            continue
        except Exception as e:
            print("Введите корректные данные")
            again_count += 1
            continue

def search_book():
    """
    Осуществляет поиск книги по заданному полю (название, автор или год).
    Запрашивает поле и значение для поиска у пользователя.
    """
    key = input("Выберите и напишите поле, по которому нужно искать (title, author, year): ")
    value = input("Введите то, что хотите искать: ")
    LibraryStorage.search_books(key, value)

def show():
    """
    Выводит список всех книг, хранящихся в библиотеке.
    """
    LibraryStorage.show_all()

def update_status():
    """
    Обновляет статус книги (в наличии или выдана) по её ID.
    Допускает три попытки ввода корректного ID, после чего завершает выполнение.

    Исключения:
        ValueError: Если пользователь ввел некорректный ID.
        Exception: Любая другая ошибка ввода.
    """
    again_count = 0
    while True:
        if again_count > 3:
            clear_console()
            print("У вас было три попытка. Начинайте все с начала в целях безопасности")
            break
        try:
            id = int(input("Введите ID книги, которую нужно обновить: "))
            if id <= 0:
                print("ID должен быть положительным числом")
                again_count += 1
                continue
            else:
                break
        except ValueError:
            print("Введите число")
            again_count += 1
            continue
        except Exception as e:
            print("Введите корректные данные")
            again_count += 1
            continue
    status = input("Выберите статус - 'в наличии' или 'выдана': ")
    LibraryStorage.update_book_status(id, status)

def command_done(command_num):
    """
    Выполняет команду, выбранную пользователем из меню.
    :param command_num: Номер команды (1-5).
    """
    clear_console()
    if command_num == 1:
        add_book()
    if command_num == 2:
        delete_book()
    if command_num == 3:
        search_book()
    if command_num == 4:
        show()
    if command_num == 5:
        update_status()

def clear_console():
    """
    Очищает консоль.
    Работает как для Windows, так и для Unix/Linux/MacOS.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_menu():
    """
    Выводит меню команд для взаимодействия с библиотекой.
    """
    print("""
Выберите команду:
1. Добавить книгу — добавить новую книгу в библиотеку.
2. Удалить книгу — удалить книгу по её ID.
3. Найти книгу — найти книгу по названию, автору или году.
4. Показать все книги — вывести список всех книг.
5. Обновить статус книги — изменить статус на 'в наличии' или 'выдана'.
0. Выйти — завершить работу программы.
""")

def main():
    """
    Главная функция программы.
    Реализует меню для взаимодействия с пользователем.
    Позволяет выбирать команды, выполнять действия или завершить программу.
    """
    while True:
        try:
            print_menu()
            command_num = int(input("Введите команду: "))
            if 0 <= command_num <= 5:
                if command_num == 0:
                    clear_console()
                    print("Ваш выход успешно выполнен")
                    break
                else:
                    clear_console()
                    command_done(command_num)
            else:
                clear_console()
                print("Введите число от 0 до 5 включительно")
        except ValueError:
            clear_console()
            print("Введите число")
            continue

if __name__ == '__main__':
    main()