
import random
from faker import Faker
from db import connection
from datetime import datetime

faker = Faker()

genres = ["Mystery", "Adventure", "Fantasy"]

adjectives = ["Dark", "Forbidden", "Mysterious", "Hidden", "Eternal"]

nouns = ["Secrets", "Kingdom", "Journey", "Love", "Shadow"]



def generate_random_dob():
    return faker.date_between(start_date=datetime(1950,1,1), end_date=datetime(2000,1,1))



def generate_random_genre():
    return random.choice(genres)



def generate_random_author():
    return faker.name()



def generate_book_title(book_genre, book_author):

    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    return f"{adjective} {noun}: a {book_genre} story by {book_author}"



def insert_user(con, name, date_of_birth):

    cursor = con.cursor()
    cursor.execute("INSERT INTO users(name, dob) VALUES (%s, %s)", (name, dob))
    con.commit()
    cursor.close()


def insert_book(con, name, book_genre, book_author):

    cursor = con.cursor()
    cursor.execute("INSERT INTO books (name, category, author) VALUES (%s, %s, %s)", (name, book_genre, book_author))
    con.commit()
    cursor.close()



dob = generate_random_dob()
genre = generate_random_genre()
author = generate_random_author()
book_title = generate_book_title(genre, author)
insert_user(connection, author, dob)
insert_book(connection, book_title, genre, author)

print(dob, genre, author, book_title)
