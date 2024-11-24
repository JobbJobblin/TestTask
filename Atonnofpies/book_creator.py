import json
import os

class Book_creator:
    """Базовый класс для всех книг библиотеки"""

    def __init__(self, title="", author="", year=None):

        self.Assign_ID()

        if title == "":
            self.Title = "Unknown Title"
        elif not isinstance(title, str):
            raise ValueError("Внимание! Введён неправильный формат данных в поле 'название книги'. Попробуйте ещё раз!")
        else:
            self.Title = title

        if author == "":
            self.Author = "Unknown Author"
        elif not isinstance(author, str):
            raise ValueError("Внимание! Введён неправильный формат данных в поле 'автор'. Попробуйте ещё раз!")
        else:
            self.Author = author

        if year == None:
            self.Year = "Unknown Year"
        elif not isinstance(year, int):
            raise ValueError("Внимание! Введён неправильный формат данных в поле 'год'. Попробуйте ещё раз!")
        else:
            self.Year = year

        self.Status = "Available"

    def Assign_ID(self, filepath = f"{os.path.dirname(os.getcwd())}\library.json"):
        try:
            with open(filepath, 'r') as f:
                try:
                    data = json.load(f)
                    self.ID = max(book["ID"] for book in data) + 1 if data else 1
                    print(f'ID is {self.ID}')
                except json.JSONDecodeError as e:
                    print(f"Ошибка json - {e}")
                    self.ID = 1
                    print(f'ID is {self.ID}')
        except FileNotFoundError:
            print(2)
            self.ID = 1
            print(f'ID is {self.ID}')

    def __del__(self):
        print("Book removal is complete.")
        # print("Destructor approaches you and says: 'My job here is done!'")
        # print("You feel your urge for random acts of violence is sated.")
        # print("At least for now...")

    def Saviour(self, filepath = f"{os.path.dirname(os.getcwd())}\library.json"):

        print(
            "You want to save the book with the following parameters: \n"
            f"Title: {self.Title}\n"
            f"Author: {self.Author}\n"
            f"Year: {self.Year}\n"
            "Correct?"
        )

        while True:
            User_Answer = input("Yes or No?\n")
            if User_Answer.lower() == "yes":
                try:
                    with open(filepath, 'r+') as f:
                        try:
                            data = json.load(f)
                        # Если файл пустой.
                        except json.JSONDecodeError:
                            data = []

                        if any(book['Author'] == self.Author and book['Title'] == self.Title and book['Year'] == self.Year for book in data):
                            print("We already have this book. Our superiors told us to keep only a single copy of every book. This is... 'for your convinience'. Sorry. Go on, try another one!")
                            break
                        data.append(self.__dict__)
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        print(data)

                # Создание файла, если его нет.
                except FileNotFoundError:
                    with open(filepath, 'w') as f:
                        json.dump([self.__dict__], f, indent=4)
                        data.append(self.__dict__)
                        print(data)
                print("Saving process is complete.")
                print(f"File is at {filepath}")
                return True
            elif User_Answer.lower() == "no":
                print("Saving process aborted.")
                return False
            else:
                print("It's a yes or no question. Come on, you can handle it.")


try:
    SmolPotat = Book_creator(title="boop", author="kosha",) #year="every year")
    SmolPotat.Saviour()
    # SmolPotat.invoke_book()
except ValueError as e:
    print(e)
