from Atonnofpies.book_book import Book

import json


class Book_search:
  """Класс для работы с библиотекой книг (Поиск, статус, удаление)."""
  def __init__(self, filepath: str):
    self.filepath = filepath
    self.load_books()

  def load_books(self) -> None:
    """Загружает книги из JSON-файла."""
    try:
      with open(self.filepath, 'r', encoding='utf-8') as f:
        self.books: list[Book] = [Book(book_data) for book_data in json.load(f)]
    except (FileNotFoundError, json.JSONDecodeError) as e:
      print(f"Ошибка при загрузке библиотеки: {e}")
      self.books: list[Book] = []

  def save_books(self) -> None:
    try:
      with open(self.filepath, 'w') as f:
        json.dump([book.__dict__ for book in self.books], f, indent=4, ensure_ascii=False)
    except IOError as e:
      print(f"Произошла ошибка при сохранении библиотеки: {e}")

  def search_books(self, ID: int = "", author: str ="", title: str="", year: int | str | None ="") -> list[Book]:
    """Ищет книги по критериям."""
    results: list[Book] = []
    for book in self.books:
      if ID and str(book.ID) != str(ID):
        continue
      if author and book.author.lower() != author.lower():
        continue
      if title and book.title.lower() != title.lower():
        continue
      if year and str(book.year) != str(year):
        continue
      results.append(book)
    return results

  def get_book_by_id(self, book_id: int) -> None:
    """Возвращает книгу по ID."""
    for book in self.books:
      if book.ID == book_id:
        return book
    return None

  def change_book_status(self, book_id: int) -> None:
    """Изменяет статус книги (В наличии/Выдана). Автоматически присваивает статус "Выдана", если статус не "В наличии" или "Выдана"."""
    book: Book | None = self.get_book_by_id(book_id)
    if book:
      if book.status != "В наличии" and book.status != "Выдана":
        book.status = "Выдана"
      current_status = print(f"Текущий статус книги {book.status}.")
      if book.status == "В наличии":
        while True:
          retrieve = input("Вы хотите взять эту книгу? (Да/Нет) ")
          if retrieve.lower() == "да":
            book.status = "Выдана"
            self.save_books()
            print("Держите. Не забудьте вернуть её.")
            break
          elif retrieve.lower() == "нет":
            print("Ну и пожалуйста. Не очень-то и хотелось.")
            break
          else:
            print("Нужно написать 'Да' или 'Нет'.")
      elif book.status == "Выдана":
        while True:
          retrieve = input("Вы хотите вернуть книгу? (Да/Нет) ")
          if retrieve.lower() == "да":
            book.status = "В наличии"
            self.save_books()
            print("Спасибо, что вернули её. Мне её не хватало.")
            break
          elif retrieve.lower() == "нет":
            print("Хорошо. Пусть пока ещё полежит у вас.")
            break
          else:
            print("Нужно написать 'Да' или 'Нет'.")
    else:
      print(f"Книга с ID {book_id} не найдена.")

  def delete_book(self, book_id: int) -> None:
    """Удаляет книгу."""
    accomplished: bool = False
    for book in self.books:
      if book.ID == book_id:
        while True:
          exit = input(f"Вы хотите удалить {book.title} автора {book.author}, написанную в {book.year} году. (Да/Нет) \n")
          if exit.lower() == "да":
            self.books = [book for book in self.books if book.ID != book_id]
            self.save_books()
            print(f"Книга с ID {book_id} удалена.")
            accomplished = True
            break
          elif exit.lower() == "нет":
            accomplished = True
            print("Возвращаю в меню.")
            break
          else:
            print("Пожалуйста, введите Да или Нет. \n")

      else:
        continue
    if not accomplished:
      print(f"Книга с ID {book_id} не найдена.")