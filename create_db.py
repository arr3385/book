import json, logging
from sqlalchemy.orm import sessionmaker
from models import Base, Book, engine


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def create_books():
    book = load_json('books.json')

    for oneBook in book['Books']:
        title = oneBook['title']
        id = oneBook['id']
		
        newBook = Book(title = title, id = id)
		# After I create the book, I can then add it to my session. 
        session.add(newBook)
		# commit the session to my DB.
        session.commit()

		
create_books()
