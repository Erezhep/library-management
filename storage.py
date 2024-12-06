from books import Book
from functions import truncate_text, print_on_console
import json
import os

class LibraryStorage:
    """
    Класс для управления хранилищем библиотеки книг.

    Методы:
        get_last_id(): Возвращает последний использованный ID книги.
        show_all(): Отображает все книги в хранилище.
        add_book(title, author, year, status): Добавляет новую книгу в хранилище.
        delete_book(book_id): Удаляет книгу из хранилища по её ID.
        search_books(key, value): Ищет книги по заданному ключу и значению.
        update_book_status(book_id, new_status): Обновляет статус книги по её ID.
    """    
    
    filename = "books.json"
    
    @staticmethod
    def get_last_id() -> int:
        """
        Возвращает последний использованный ID книги из хранилища.

        :return: Последний ID (int). Если данных нет, возвращает 0.
        """
        id = 0
        if os.path.exists(LibraryStorage.filename) and os.path.isfile(LibraryStorage.filename):
            try:
                with open(LibraryStorage.filename, "r", encoding = "utf-8") as f:
                    data = json.load(f)
                
                if data:
                    id = data[-1]["id"]
                
            except json.JSONDecodeError as e:
                print(f"Ошибка декодирования JSON: {e}")
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")
        else:
            print(f"Файл хранилище {LibraryStorage.filename} не найдена.")
        return id
    
    @staticmethod
    def show_all():
        """
        Отображает все книги в хранилище.

        :return: None. Выводит список книг в консоль. Если хранилище пусто, выводит сообщение.
        """
        if os.path.exists(LibraryStorage.filename) and os.path.isfile(LibraryStorage.filename):
            try:
                with open(LibraryStorage.filename, "r", encoding = "utf-8") as f:
                    data = json.load(f)
                
                if not data:
                    print("Хранилище пусто")
                else:
                    data.sort(key=lambda x: x["id"])
                    print_on_console(data)
                
            except json.JSONDecodeError as e:
                print(f"Ошибка декодирования JSON: {e}")
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")
        else:
            print(f"Файл хранилище {LibraryStorage.filename} не найдена.")
    
    @staticmethod
    def add_book(title, author, year, status = "в наличии"):
        """
        Добавляет новую книгу в хранилище.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        :param status: Статус книги ("в наличии" по умолчанию).
        :return: None. Выводит сообщение об успешном добавлении книги.
        """
        # Создаем объект книги
        book = Book(title, author, year, status)
        new_book = book.to_dict()
        new_book["id"] = LibraryStorage.get_last_id() + 1
        
        # Читаем данные из файла, если файл существует
        if os.path.exists(LibraryStorage.filename) and os.path.isfile(LibraryStorage.filename):
            try:
                with open(LibraryStorage.filename, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = []  # Если файл пустой или поврежден
        
        data.append(new_book)
        
        
        
        # Сохраняем изменения в файл
        with open(LibraryStorage.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Книга '{title}' успешно добавлена в хранилище.")
        
    @staticmethod
    def delete_book(book_id):
        """
        Удаляет книгу по её ID из хранилища.
        :param book_id: ID книги для удаления
        """
        if os.path.exists(LibraryStorage.filename) and os.path.isfile(LibraryStorage.filename):
            try:
                with open(LibraryStorage.filename, "r", encoding = "utf-8") as f:
                    data = json.load(f)
                
                if not data:
                    print("Хранилище пусто")  
                    return  
                else:
                    
                    book_exists = any(book["id"] == book_id for book in data)
                    
                    if not book_exists:
                        print(f"Книга с ID {book_id} не найдена.")
                        return
                    
                    updated_data = [book for book in data if book["id"] != book_id]
                    
                    with open(LibraryStorage.filename, "w", encoding="utf-8") as f:
                        json.dump(updated_data, f, ensure_ascii=False, indent=4)
                    
                    print(f"Книга с ID {book_id} успешно удалена.")
                
            except json.JSONDecodeError as e:
                print(f"Ошибка декодирования JSON: {e}")
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")
        else:
            print(f"Файл хранилище {LibraryStorage.filename} не найдена.")
            
    @staticmethod
    def search_books(key, value):
        """
        Ищет книги по заданному ключу и значению.
        :param key: Поле для поиска (например, "title", "author", "year")
        :param value: Значение для поиска
        :return: Список найденных книг
        """
        if os.path.exists(LibraryStorage.filename) and os.path.isfile(LibraryStorage.filename):
            try:
                # Читаем данные из файла
                with open(LibraryStorage.filename, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # Проверяем, есть ли данные в файле
                if not data:
                    print("Хранилище пусто.")
                    return

                # Фильтруем книги по ключу и значению (регистр не учитывается для строк)
                results = [
                    book for book in data
                    if str(book.get(key, "")).lower() == str(value).lower()
                ]

                if results:
                    print(f"Найдено {len(results)} книг(а):")
                    for book in results:
                        print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}")
                else:
                    print("Книги по заданным критериям не найдены.")

                return results
            
            except json.JSONDecodeError as e:
                print(f"Ошибка декодирования JSON: {e}")
                return
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")
                return
        else:
            print(f"Файл хранилища {LibraryStorage.filename} не найден.")
            return
        
    @staticmethod
    def update_book_status(book_id, new_status):
        """
        Обновляет статус книги по её ID.
        :param book_id: ID книги для обновления
        :param new_status: Новый статус книги ("в наличии" или "выдана")
        """
        if new_status not in ["в наличии", "выдана"]:
            print("Недопустимый статус. Укажите 'в наличии' или 'выдана'.")
            return

        if os.path.exists(LibraryStorage.filename) and os.path.isfile(LibraryStorage.filename):
            try:
                # Чтение данных из файла
                with open(LibraryStorage.filename, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # Проверка, есть ли данные
                if not data:
                    print("Хранилище пусто.")
                    return

                # Поиск книги с указанным ID
                book_found = False
                for book in data:
                    if book["id"] == book_id:
                        book["status"] = new_status
                        book_found = True
                        break

                if not book_found:
                    print(f"Книга с ID {book_id} не найдена.")
                    return

                # Сохранение обновленных данных обратно в файл
                with open(LibraryStorage.filename, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)

                print(f"Статус книги с ID {book_id} успешно обновлён на '{new_status}'.")
            
            except json.JSONDecodeError as e:
                print(f"Ошибка декодирования JSON: {e}")
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")
        else:
            print(f"Файл хранилища {LibraryStorage.filename} не найден.")