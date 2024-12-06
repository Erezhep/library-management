class Book:

    def __init__(self, title, author, year, status="в наличии"):
        """
        Класс для представления книги.
        :param title: название книги
        :param author: автор книги
        :param year: год издания книги
        :param status: статус книги (по умолчанию "в наличии")
        """
        self.title = title
        self.author = author
        self.year = year
        self.status = status


    def to_dict(self):
        """
        Преобразует объект книги в словарь для сохранения в файл.
        """
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }