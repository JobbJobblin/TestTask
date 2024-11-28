import json

class Book_creator:

    def __init__(self, title="", author="", year=None, filepath = ""):

        try:
            self.Assign_ID(filepath)

            if title == "":
                self.Title = "Без названия"
            elif not isinstance(title, str):
                raise ValueError("Неверный формат поля 'Наименование'.")
            else:
                self.Title = title

            if author == "":
                self.Author = "Неизвестный автор"
            elif not isinstance(author, str):
                raise ValueError("Неверный формат поля 'Автор'.")
            else:
                self.Author = author

            if year == "" or year == None:
                self.Year = "Год неизвестен"
            elif not isinstance(year, int):
                raise ValueError("Неверный формат поля 'Год'.")
            else:
                self.Year = year

            self.Status = "В наличии"
        except ValueError as e:
            print(f"Ошибка: {e}")

    def Assign_ID(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    self.ID = max(book["ID"] for book in data) + 1 if data else 1
                except json.JSONDecodeError as e:
                    print(f"Ошибка json - {e}")
                    self.ID = 1
        except FileNotFoundError:
            self.ID = 1

    def __del__(self):
        print("Память освобождена.")

    def Saviour(self, filepath):
        """Сохраняет книгу в JSON-файл с латинскими ключами."""

        print(
            "Вы хотите сохранить книгу со следующими параметрами: \n"
            f"Название: {self.Title}\n"
            f"Автор: {self.Author}\n"
            f"Год: {self.Year}\n"
            "Верно?"
        )

        while True:  # Более чистый цикл while
            user_answer = input("Введите, пожалуйста, ваш ответ (Да/Нет)\n").lower()
            if user_answer == "да":
                try:
                    with open(filepath, 'r+', encoding='utf-8') as f:
                        try:
                            data = json.load(f)
                        except json.JSONDecodeError:
                            data = []

                        # Проверка на дубликаты
                        if any(book['author'] == self.Author and book['title'] == self.Title and book[
                            'year'] == self.Year for book in data):
                            print("Эта книга уже есть в библиотеке. Попробуйте другую.")
                            return # Возвращаем в меню

                        # Создаем словарь с латинскими ключами
                        book_data = {
                            "ID": self.ID,
                            "title": self.Title,
                            "author": self.Author,
                            "year": self.Year,
                            "status": self.Status
                        }
                        data.append(book_data)

                        f.seek(0)  # Перемещаем курсор в начало файла
                        json.dump(data, f, indent=4, ensure_ascii=False)  # ensure_ascii=False для кириллицы
                        f.truncate()  # Удаляем остатки старого содержимого

                    print("Сохранено.")
                    print(f"Ваша книга лежит в {filepath}")
                    return True  # Возвращаем True, если сохранение успешно

                except FileNotFoundError:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump([{'ID': self.ID, 'title': self.Title, 'author': self.Author, 'year': self.Year,
                                    'status': self.Status}], f, indent=4, ensure_ascii=False)
                    print("Сохранено.")
                    print(f"Ваша книга лежит в {filepath}")
                    return True  # Возвращаем True, если сохранение успешно

            elif user_answer == "нет":
                print("Процесс сохранения отменён.")
                return False  # Возвращаем False, если сохранение отменено

            else:
                print("Нужно написать 'Да' или 'Нет'.")