def validate_book_data(data: dict) -> bool:
    """
    Проверка корректности данных книги. 
    Обязательные поля присутствуют и корректны.
    """
    title = data['title']
    if not title:
        return False
    elif not isinstance(title, str):
        return False
    
    author = data['author']
    if not author:
        return False
    elif not isinstance(author, str):
        return False 

    genre = data['genre']
    if not genre:
        return False
    elif not isinstance(genre, str):
        return False 
    
    return True
