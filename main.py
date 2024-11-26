from library_manager.catalog import Library

library = Library()
# Добавление книг
library.add_book("1984", "George Orwell", "Dystopian")
library.add_book("Brave New World", "Aldous Huxley", "Science Fiction")
library.add_book("Fahrenheit 451", "Ray Bradbury", "Dystopian")

print("\nВсе книги:")
library.show_books()

# Поиск книг
print("\nПоиск книг по жанру 'Dystopian':")
found_books = library.search_book(genre="Dystopian")
for book in found_books:
    print(book)

# Удаление книги
library.remove_book("1984")
print("\nВсе книги после удаления:")
library.show_books()

# Попытка удалить несуществующую книгу
library.remove_book("Nonexistent Book")

