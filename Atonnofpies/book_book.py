import json
import os

class Book:
  """Базовый класс для всех книг библиотеки"""
  def __init__(self, book_data: dict):
    self.ID = book_data['ID']
    self.title = book_data['title']
    self.author = book_data['author']
    self.year = book_data['year']
    self.status = book_data['status']


  def __str__(self) -> str:
    return f"ID: {self.ID}, Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {self.status}"

