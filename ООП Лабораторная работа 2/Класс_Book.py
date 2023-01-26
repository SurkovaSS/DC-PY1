import doctest
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_:int, name:str, pages:int):
        '''
        Создание и подготовка к работе объекта Book
        :param id_: идентификационный номер книги
        :param name: Название книги
        :param pages: Колличество страниц в книге

        Примеры:
        >>> book = Book(2,'War and Peace', 1225) # Инициализация экземпляра класса
        '''
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        '''
        Строковый метод класса Book.
        :return: Книга с её названием

        Примеры:
        >>> book = Book(2,'War and Peace', 1225)
        >>> print(book)
        Книга "War and Peace"
        '''
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        '''
        Еще один строковый метод, но который возвращает валидную питоновскую строку
        :return: #Питоновская строка, которой можно инициализировать объект

        Примеры:
        >>> book = Book(2,'War and Peace', 1225)
        >>> print(repr(book))
        Book(id_=2, name='War and Peace', pages=1225)
        '''
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


if __name__ == '__main__':
    doctest.testmod()
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
