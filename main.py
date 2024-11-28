import os

from Atonnofpies.book_search import Book_search
from Atonnofpies.book_creator import Book_creator


def main():
    """Главная функция программы."""
    filepath = "library.json"
    library = Book_search(filepath)

    while True:
        print("\nМеню библиотеки:")
        print("1. Добавить книгу в библиотеку")
        print("2. Показать список всех книг")
        print("3. Поиск книг")
        print("4. Изменить статус книги")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Что вы хотите сделать: \n")

        if choice == '1':
            success: bool = False  # Флаг успешного выполнения
            while not success:
                try:
                    author: str = input("Введите ФИО автора (опционально): \n")
                    title: str = input("Введите название книги (опционально): \n")
                    year_str: str = input("Введите год (опционально): \n")  # Ввод как строка для обработки
                    year: int|None|str = None
                    try:
                        year = int(year_str.strip())  # Преобразование в целое число только если строка не пустая
                    except:
                        raise ValueError("Неверный формат поля 'год'")
                    creation = Book_creator(title.strip(), author.strip(), year, filepath)  # создание объекта
                    creation.Saviour(filepath)  # Сохранение книги
                    success = True  # Установка флага на True после успешного выполнения
                except ValueError as e:
                    print(f"Ошибка при создании книги: {e}")
                    while True:
                        exit = input("Попробовать ещё раз? (Да/Нет) \n")
                        if exit.lower() == "да":
                            break
                        elif exit.lower() == "нет":
                            success = True
                            print("Возвращаю в меню.")
                            break
                        else:
                            print("Пожалуйста, введите Да или Нет. \n")

                except Exception as e:  # Обработка других возможных ошибок
                    print(f"Произошла неизвестная ошибка: {e}")
                    while True:
                        exit = input("Попробовать ещё раз? (Да/Нет) \n")
                        if exit.lower() == "да":
                            break
                        elif exit.lower() == "нет":
                            success = True
                            print("Возвращаю в меню.")
                            break
                        else:
                            print("Пожалуйста, введите Да или Нет. \n")
            library = Book_search(filepath) #Перезагрузить список книг, чтобы остальные функции срабатывали с добавленной книгой

        elif choice == '2':
            found_books = library.search_books()
            if found_books:
                for book in found_books:
                    print(book)
            else:
                print("Библиотека пуста.")

        elif choice == '3':
            success: bool = False
            while not success:
                try:
                    id_str: str = input("Введите ID книги в нашей библиотеке (опционально): \n")
                    ID: int|None = None
                    if id_str.strip():  # Проверка на пустую строку
                        try:
                            ID = int(id_str.strip()) # Преобразование в целое число только если строка не пустая
                        except:
                            raise ValueError ("Неверный формат поля 'ID'")
                    author: str = input("Введите ФИО автора (опционально): \n")
                    title: str = input("Введите название книги (опционально): \n")
                    year_str: str = input("Введите год (опционально): \n")  # Ввод как строка для обработки
                    year: str|int|None = None
                    if year_str.strip() and year_str.strip() != "Год неизвестен":  # Проверка на пустую строку
                        try:
                            year = int(year_str.strip()) # Преобразование в целое число только если строка не пустая
                        except:
                            raise ValueError ("Неверный формат поля 'год'")
                    elif year_str.strip() == "Год неизвестен": #Исключение для неизвестного года
                        year = year_str.strip()
                    found_books = library.search_books(ID, author.strip(), title.strip(), year)
                    if found_books:
                        for book in found_books:
                            print(book)
                    else:
                        print(f"Извините, но книги, подходящей под ваше описание ('{ID}', '{author}', '{title}', '{year}'), у нас нет.")
                    success = True
                except ValueError as e:
                    print(f"Неверный формат ввода. {e}")
                    while True:
                        exit = input("Попробовать ещё раз? (Да/Нет) \n")
                        if exit.lower() == "да":
                            break
                        elif exit.lower() == "нет":
                            success = True
                            print("Возвращаю в меню.")
                            break
                        else:
                            print("Пожалуйста, введите Да или Нет. \n")

                except Exception as e:
                    print(f"Произошла неизвестная ошибка {e}")
                    while True:
                        exit = input("Попробовать ещё раз? (Да/Нет) \n")
                        if exit.lower() == "да":
                            break
                        elif exit.lower() == "нет":
                            success = True
                            print("Возвращаю в меню.")
                            break
                        else:
                            print("Пожалуйста, введите Да или Нет. \n")
        elif choice == '4':
            book_id: int = int(input("Введите ID книги: \n"))
            library.change_book_status(book_id)
            library = Book_search(filepath)

        elif choice == '5':
            book_id: int = int(input("Введите ID книги: \n"))
            library.delete_book(book_id)
            library = Book_search(filepath)

        elif choice == '6':
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите один из вариантов меню.")


if __name__ == "__main__":
    main()
