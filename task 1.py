class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str :
        return self._name

    @property
    def author(self) -> str:
        return self._author

    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError('name must be str type')

    @author.setter
    def author(self, author: str) -> None:
        if isinstance(author, str):
            self._author = author
        else:
            raise TypeError('author must be str type')


    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if isinstance(new_pages, int):
            self._pages = new_pages
        else:
            raise TypeError('pages must be int type')

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if isinstance(new_duration, float):
            self._duration = new_duration
        else:
            raise TypeError('duration must be float type')

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"

