from classes.library import Library


class Menu:
    def __init__(self):
        self.library = Library()
        self.choices = {
            "1": self.show_lib,
            "2": self.add_book,
            "3": self.add_audio_book,
            "4": self.add_dvd,
            "5": self.modify_lib,
            "6": self.quit
        }

    def display_menu(self):
        print(
            """
            Notebook Menu
            1. Show all Books
            2. Add Book
            3. Add Audio Book
            4. Add DVD
            5. Modify Library
            6. Quit
            """
        )

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_lib(self):
        if len(self.library.library.keys()) == 3:
            print("Library is empty!")
        else:
            while True:
                question = input("Axlaaaa duuyureeee Would You Like To See List Of Books, Audio Books, or DVD? >> ")
                if question == "Books":
                    self.library.info("book")
                    return
                elif question == "Audio Books":
                    self.library.info("audioBook")
                    return
                elif question == "DVD":
                    self.library.info("DVD")
                    return
                elif question.isdigit():
                    print("Please Enter Only Books, Audio Books, or DVD >> ")
                    continue

    def add_book(self):
        title = input("Enter Title Of Book >> ")
        genre = input("Enter Genre of Book >> ")
        self.library.add_new_item_book(title, genre)
        print("book has been added!")

    def add_audio_book(self):
        title = input("Enter Title Of Audio Book >> ")
        genre = input("Enter Genre of Audio Book >> ")
        self.library.add_new_item_audio_book(title, genre)
        print("Audio Book has been added!")

    def add_dvd(self):
        title = input("Enter Title Of Audio DVD >> ")
        genre = input("Enter Genre of Audio DVD >> ")
        self.library.add_new_item_dvd(title, genre)
        print("DVD has been added!")

    def modify_lib(self):
        print(len(self.library.library.keys()))
        if len(self.library.library.keys()) == 3:
            print("Theres nothing to modify")
        else:
            target = input("Would you like to modify Book, Audio Book, or DVD ? >>> ")
            id_to_modify = int(input("Enter id of item to modify >>> "))
            title = input("Choose new title >>> ")
            genre = input("Choose Genre >>> ")
            self.library.modify(target, id_to_modify, title, genre)
            print("Proccess Finished sakaifod")

    def quit(self):
        print("Thank you for using your library today.")


if __name__ == "__main__":
    Menu().run()
