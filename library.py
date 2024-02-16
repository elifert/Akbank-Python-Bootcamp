class BookNotFoundError(Exception):
    def __str__(self):
        return "The book title you entered has not been added to the Library Management system yet.\nTo see the available books, please enter 1."


class Library:
    def __init__(self):
        self.file = open("books.txt", "a+", encoding="utf-8")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        contents = self.file.read().splitlines()
        for i in range(len(contents)):
            title, author, _, _ = contents[i].split(",")
            print(f"Book: {title}, Author: {author}")

    def add_book(self):
        title = input("Enter the book title: ").title()
        author = input("Enter the author: ").title()
        release_year = input("Enter the first release year: ")
        page_numbers = input("Enter the number of pages: ")
        self.file.write(f"{title},{author},{release_year},{page_numbers}\n")

    def remove_book(self):
        title = input("Enter the book title to remove: ").title()
        found = False
        self.file.seek(0)
        contents = self.file.read().splitlines()
        for index, element in enumerate(contents):
            if title in element:
                contents.pop(index)
                found = True
                break
        if not found:
            raise BookNotFoundError
        new_contents = [element + "\n" for element in contents]
        self.file.truncate(0)
        self.file.writelines(new_contents)


def main():
    lib = Library()
    choices = {
        "1": lib.list_books,
        "2": lib.add_book,
        "3": lib.remove_book,
    }

    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "q":
            break
        else:
            try:
                choices[choice]()
            except KeyError:
                print("Invalid choice. Please try again.")
            except BookNotFoundError as message:
                print(message)


def menu():
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Books")
    print("3) Remove Books")
    print("q) Quit")


if __name__ == "__main__":
    main()
