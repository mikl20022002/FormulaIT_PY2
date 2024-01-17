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
        """
        создает экземпляр класса book и задает атрибуты

        :id_: id данной книги
        :name: название данной книги
        :pages: количество страниц данной книги
        """
        self.id_ = id_
        self.name = name
        self.pages = pages


    def __str__(self):
        """
        :return: возвращает строковое представление экземпляра, понятное человеку
        """
        return f'Книга "{self.name}"'


    def __repr__(self):
        """
        :return: возвращает валидную python строку
        """
        return f'Book(id_={self.id_}, name={self.name!r}, pages={self.pages})'

# TODO написать класс Library
class Library:
    def __init__(self, books:list=None):
        """
        Создает экземпляр класса library и задает атрибуты.
        Данный класс хранит список книг и содержит методы для работы с ними

        :books: список из экземпляров класса Book
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        """
        :return: возвращает индекс свободного места для добавления книги
        """
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_to_find: int) -> int:
        """
        :id_to_find: id книги которую требуется найти
        :return: если книга есть в списке - возвращает позицию искомой книги
                 если книге нет в списке - поднимает ошибку ValueError
        """
        for i, book in enumerate(self.books):
            if book.id_ == id_to_find:
                return i
        raise ValueError('Книги с запращиваемым id не существует')


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
