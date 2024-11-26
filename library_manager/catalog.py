from .utils.formatting import format_book_data
class Library:
    '''
    Класс для управления библиотекой: добавление книг, удаление книг 
    и поиск книг в библиотеке по названию
    '''
    def __init__(self):
       """Инициализация библиотеки с пустым списком книг"""
       self._library = [] 

    def __str__(self):
        return f'Библиотека: {self._library}'
    
    def add_book(self, title, author, genre):
        """Добавление книги в библиотеку"""
        new_book = {"title": title,"author": author, "genre": genre}
        self._library.append(new_book) # добавляем книгу
        print(f"Книга '{title}' добавлена в библиотеку.")

    def remove_book(self, title):
        """ Удаление книги из библиотеки"""
        for book in self._library:
            if book['title'] == title:
                self._library.remove(book)
                print(f"Книга {title} удалена из библиотеки. ")

    def search_book(self, **kwargs):
        """ 
        Поиск книги по переданным параметрам.
        kwargs может содержать 'title', 'author', 'genre'
        """
        results = []
        for key, value in kwargs.items():
            results = [book for book in self._library if book.get(key) == value]
        return results
    
    def show_books(self):
        """Вывод всех книг в библиотеке"""
        if not self._library:
            print("Библиотека пуста.")
        else:
            for book in self._library:
                print(format_book_data(book))
                #print(f"Название: {book['title']}, Автор: {book['author']}, Жанр: {book['genre']}")

