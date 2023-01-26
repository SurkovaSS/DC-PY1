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
    def __init__(self, id_: int, name: str, pages: int):
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


# TODO написать класс Library
class Library:
    def __init__(self, books: list = None):
        '''
        Создание и подготовка к работе объекта Library
        :param books: книги, которые лежат в библиотеке

        Примеры:
        >>> empty_library = Library() # Инициализируем пустую библиотеку
        >>> list_books = [Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE] # Список книг
        >>> library_with_books = Library(books=list_books) # Инициализируем библиотеку с книгами
        '''
        self.books = books
        self.list_of_ids = []
        if self.books is not None:
            self.list_of_ids = [book.__dict__['id'] for book in self.books]

    def get_next_book_id(self) -> int:
        '''
        Данный метод возвращиет идентификатор для добавления новой книги в библиотеку
        :return: идентификатор

        Примеры
        >>> empty_library = Library()
        >>> empty_library.get_next_book_id()
        1
        '''
        if not self.books:
            return 1
        return self.books[-1].__dict__['id'] + 1

    def get_index_by_book_id(self, id) -> int:
        '''
        Данный метод возвращет индекс книги в списке библиотечных книг,
        котрый хранится в атрибуте self.list_of_ids экземпляра класса
        :param id: идентификатор запрашиваемо книги
        :return: номер в списке библиотечных книг

        Примеры:
        >>> list_books = [Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE]
        >>> library_with_books = Library(books=list_books) # Инициализируем библиотеку в 2 книгами
        >>> library_with_books.get_index_by_book_id(1) # Ищем книгу с идентификатором 1
        0
        '''
        for index, value in enumerate(self.list_of_ids):
            if value == id:
                return index
        return ValueError('Книги с запрашиваемым id не существует')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
    doctest.testmod()
