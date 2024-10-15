#napravili smo praznu listu knjiga, def za dodavanje, def za pretrazivanje i def sa brisanje knjige
books = []

def add_book(book_name, book_author):
    books.append({"name": book_name, "author": book_author})


def find_book_by_name(name):
    for book in books:
        if book["name"] == name:
            return book


find_book_by_name("Harry Potter 1")
print(books)

add_book("Harry Potter 1", "J. K. Rowling")
add_book("Harry Potter 3", "J. K. Rowling")

hp1 = find_book_by_name("Harry Potter 1")

if hp1 is None:
    print("Nema ove knjige!")


def delete_book_by_name(book_name):

     found_book = find_book_by_name(book_name)
    if found_book is None:
        print("Knjiga koju trazite ne postoji!")
    else:
        books.remove(found_book)
        print("Obrisana je knjiga!")


delete_book_by_name("Harry Potter 3")
print(books)





