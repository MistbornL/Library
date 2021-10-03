from service.search_for_modify import search_to_modify
from service.appendData import append_data
from classes.AudioBooks import AudioBooks
from classes.Book import Books
from classes.DVD import DVD


class Library:
    def __init__(self):
        self.library = {
            "book": [

            ],

            "audioBook": [

            ],

            "DVD": [

            ]

        }

    def add_new_item_book(self, title, genre):
        book = Books(title, genre)
        append_data(book, self.library, 'book')

    def add_new_item_audio_book(self, title, genre):
        audio_book = AudioBooks(title, genre)
        append_data(audio_book, self.library, 'audioBook')

    def add_new_item_dvd(self, title, genre):
        dvd = DVD(title, genre)
        append_data(dvd, self.library, 'DVD')

    def modify(self, target: str, id_to_modify: int, title, genre):
        books = self.library['book']
        audio_book = self.library['audioBook']
        dvd = self.library['DVD']
        if target == "Books":
            search_to_modify(books, id_to_modify, title, genre)
        elif target == "Audio Books":
            search_to_modify(audio_book, id_to_modify, title, genre)
        elif target == "DVD":
            search_to_modify(dvd, id_to_modify, title, genre)

    def delete(self, id_to_delete: int, target: str):
        item = self.library[target]
        item.pop(id_to_delete - 1)
        return self.library

    def info(self, target):
        item = self.library[target]
        for each in item:
            print(f'Title: {each["title"]}, Genre: {each["genre"]}')
