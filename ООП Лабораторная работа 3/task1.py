import doctest
class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        '''
        Создание и подготовка к работе объекта Book
        :param name: Название книги
        :param author: Автор книги

        Примеры:
        >>> book = Book('War and Peace', 'Leo Tolstoy') # Инициализация экземпляра класса
        '''
        self._name = name
        self._author = author

    def __str__(self) -> str:
        '''
        Строковый метод класса Book
        :return: возвращает название книги и её автора

        Примеры:
        >>> book = Book('War and Peace', 'Leo Tolstoy')
        >>> print(book)
        Книга War and Peace. Автор Leo Tolstoy.
        '''
        return f"Книга {self.name}. Автор {self.author}."

    def __repr__(self) -> str:
        '''
        Еще один строковый метод, но который возвращает валидную питоновскую строку
        :return: Питоновская строка, которой можно инициализировать объект

        Примеры:
        >>> book = Book('War and Peace', 'Leo Tolstoy')
        >>> print(repr(book))
        Book(name='War and Peace', author='Leo Tolstoy')
        '''
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        '''
        Делает приватный атрибут _name свойством name.
        :return: Возвращает значение свойства name

        Примеры:
        >>> book = Book('War and Peace', 'Leo Tolstoy')
        >>> print(book.name)
        War and Peace
        '''
        return self._name

    @property
    def author(self) -> str:
        '''
        Делает приватный атрибут _author свойством author
        :return: Возвращает значение для свойства author

        Примеры:
        >>> book = Book('War and Peace', 'Leo Tolstoy')
        >>> print(book.author)
        Leo Tolstoy
        '''
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        '''
        Создание и подготовка к работе объекта PaperBook
        :param name: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры
        >>> book = PaperBook('War and Peace', 'Leo Tolstoy', 1225) # Инициализация экземпляра класса
        '''
        super().__init__(name, author)
        self._pages = pages

    def __str__(self):
        '''
        Строковый метод класса Book
        :return: возвращает название книги и её автора

        Примеры:
        >>> book = PaperBook('War and Peace', 'Leo Tolstoy', 1225)
        >>> print(book)
        Бумажная книга War and Peace. Автор Leo Tolstoy.
        '''
        return f"Бумажная книга {self.name}. Автор {self.author}."

    @property
    def pages(self) -> int:
        '''
        Делает приватный атрибут _pages свойством pages
        :return: Возвращает значение свойства pages

        Примеры
        >>> book = PaperBook('War and Peace', 'Leo Tolstoy', 1225)
        >>> print(book.pages)
        1225
        '''
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        '''
        Сэттер для свойства pages
        :param pages: Новое значение для свойства pages
        :return: Ничего не возвращает. Присваивает новое значение для свойства pages

        Примеры
        >>> book = PaperBook('War and Peace', 'Leo Tolstoy', 1225)
        >>> book.pages = 'string'
        TypeError
        >>> book.pages = -1
        ValueError
        >>> book.pages = 1226
        '''
        if not isinstance(new_pages,int):
            raise TypeError
        if new_pages < 1:
            raise ValueError
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        '''
        Создание и подготовка к работе объекта AudioBook
        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность книги

        Примеры:
        >>> book = AudioBook('Harry Potter', 'Joanne Rowling', 15.133)
        '''
        super().__init__(name, author)
        self._duration = duration

    def __str__(self):
        '''
        Строковый метод класса Book
        :return: возвращает название книги и её автора

        Примеры:
        >>> book = AudioBook('Harry Potter', 'Joanne Rowling', 15.133)
        >>> print(book)
        Аудиокнига Harry Potter. Автор Joanne Rowling.
        '''
        return f"Аудиокнига {self.name}. Автор {self.author}."

    @property
    def duration(self) -> float:
        '''
        Делает атрибут _duration свойством
        :return: Возвращает значене атрибута duration

        Примеры:
        >>> book = AudioBook('Harry Potter', 'Joanne Rowling', 15.133)
        >>> print(book.duration)
        15.133
        '''
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        '''
        Сэттер свойства duration
        :param duration: Новое значение для свойства duration
        :return: Ничего не возвращает. Присваивает новое значение для свойства duration

        Примеры:
        >>> book = AudioBook('Harry Potter', 'Joanne Rowling', 15.133)
        >>> book.duration = 'string'
        TypeError
        >>> book.duration =
        '''
        if not isinstance(new_duration, float):
            raise TypeError
        if not new_duration > 0:
            raise ValueError
        self._duration = new_duration


if __name__ == '__main__':
    doctest.testmod()
    # book = PaperBook('War and Peace', 'Leo Tolstoy', 1225)
    # print(book)
    # print(repr(book))
    # ebook = AudioBook('Harry Potter', 'Joanne Rowling', 15.133)
    # print(ebook)
    # print(repr(ebook))