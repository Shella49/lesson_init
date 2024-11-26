from catalog import Library
from .utils.formatting import format_book_data

def generate_report(library: Library)-> str:
    """Вывод всех книг в библиотеке"""
    if not library:
        print("Библиотека пуста.")
        return []
    else:
        out = f"Полный список книг в библиотеке:\n"
        for book in library:
            out += format_book_data(book) + '\n'
            #print(f"Название: {book['title']}, Автор: {book['author']}, Жанр: {book['genre']} ")
    return out