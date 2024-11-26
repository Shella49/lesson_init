def format_book_data(data :dict)-> str:
    """
    Форматирует данные книги для вывода в отчет.
    """
    return f"Title: {data['title']}, Author: {data['author']}, Ganre: {data['genre']}"
