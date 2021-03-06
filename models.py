'''
This file defines the models for a book
'''
# for manipulating diff parts of Python's run-time environment
import sys
import os
# for writing mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base 

# for writing mapper code (create out foreign key relationship)
from sqlalchemy.orm import relationship

# for configuring code at the end of the file
from sqlalchemy import create_engine


# for creating an instance of the declarative_base class
# (the declarative base class will let SQLAlchemy know 
# that our classes are special SQLAlchemy classes that 
# corresponds to tables in our DB)
Base = declarative_base()

class Book(Base):
	__tablename__ = 'book'
	
	title = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:asd123@localhost/bookdb')
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# try to run this file:
# python create_db.py
# you may receive the following error:
# ImportError: No module named 'psycopg2'
# This indicates that you need to install 'psycopg2' module
# To install the 'psycopg2' module:
# pip install psycopg2

