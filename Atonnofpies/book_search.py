import json
import os

class Book_search:

    def __init__(self):
        print("poop")

    def track_book(self, filepath=f"{os.path.dirname(os.getcwd())}\library.json", Author="", Title="", Year=""):
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                found_books = []
                for book in data:
                    if Author and book['Author'].lower() != Author.lower():
                        continue
                    if Title and book['Title'].lower() != Title.lower():
                        continue
                    if Year and book['Year'] != str(Year):  # Преобразуем Year в строку для сравнения
                        continue
                    found_books.append(book)

                if found_books:
                    print("We have found...:")
                    for book in found_books:
                        print(
                            f"ID: {book['ID']}, Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year']}")
                else:
                    print("None of our books match your description. You should brink one to us!")
        except FileNotFoundError:
            print("There's no library. Which is weird...")
        except json.JSONDecodeError:
            print("Can't read library file. Can't. Read. Library. That's some extraordinary level of irony.")

        User_Task = input('What do you want to do with it?\n'
            'Available commands:\n'
            'Status\n'
            'Delete\n'
              )

        while True:
            if User_Task.lower() == "status":
                self.StatusBook()
                return
            elif User_Task.lower() == "delete":
                self.DeleteBook()
                return
            else:
                User_Task = input("Just write the word 'status' or 'delete'. Please...\n")

    @staticmethod
    def load_from_file(book_id = "", filepath=f"{os.path.dirname(os.getcwd())}\library.json", book_author = "", book_title = "", book_year = ""):
        """Загружает книгу из JSON-файла по ID."""
        try:
            with open(filepath, 'r') as f:
                try:
                    data = json.load(f)
                    matching_books = []
                    for book_data in data:
                        match = True
                        if book_id:
                            match = match and (book_data['ID'] == int(book_id))
                        if book_author:
                            match = match and (book_data['Author'] == book_author)
                        if book_title:
                            match = match and (book_data['Title'] == book_title)
                        if book_year:
                            match = match and (book_data['Year'] == book_year)
                        if match:
                            book = Book()
                            book.__dict__.update(book_data)
                            matching_books.append(book)
                    return matching_books  # Возвращаем список книг
                except json.JSONDecodeError:
                    return None
        except FileNotFoundError:
            return None

    def StatusBook(self, filepath = f"{os.path.dirname(os.getcwd())}\library.json"):

        print(f"The book is {self.Status} now")

        if self.Status == "Available":
            User_Task = input ("Do you want to take it? (Yes/No)")

            while True:
                if User_Task.lower() == "yes":
                    self.Status = "Taken"
                    self.save_to_file(filepath)
                    print(f"The book is {self.Status} now")
                    return
                elif User_Task.lower() == "no":
                    print("Fine.")
                    return
                else:
                    User_Task = input("It's a yes or no question. Type 'yes' or 'no'.\n")

        else:
            User_Task = input ("Do you want to return the book? (Yes/No)")

            while True:
                if User_Task.lower() == "yes":
                    self.Status = "Available"
                    self.save_to_file(filepath)
                    print(f"The book is {self.Status} now")
                    return
                elif User_Task.lower() == "no":
                    print("Fine.")
                    return
                else:
                    User_Task = input("It's a yes or no question. Type 'yes' or 'no'.\n")

    def save_to_file(self, filepath = f"{os.path.dirname(os.getcwd())}\library.json"):
        try:
            with open(filepath, 'r+') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []

                # Находим книгу и меняем ее статус
                for book_data in data:
                    if book_data['ID'] == self.ID:
                        book_data['Status'] = self.Status  # Обновляем статус
                        break  # Выходим из цикла после обновления

                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")




    def DeleteBook(self):
        print("The book has been removed. ")



    def Asking_Alexandria(self):
        print("")







coursor = Book_search()