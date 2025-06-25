from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Data/duombaze.db')
session_maker = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    """
    Base class for SQLAlchemy models.
    This class is used to define the base for all models in the application.
    It inherits from DeclarativeBase, which is a SQLAlchemy class that provides
    a declarative mapping system.
    """
    CreatedBy = Column(String(50), nullable=False, default='System')
    pass

class Book(Base):
    """
    Book model class.
    This class represents a book in the database.
    It inherits from Base, which is the base class for all SQLAlchemy models.
    """
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}')>"
    def __str__(self):
        return f"Book: {self.title} by {self.author}, published in {self.year}"

# create reader
class Reader(Base):
    """
    Reader model class.
    This class represents a reader in the database.
    It inherits from Base, which is the base class for all SQLAlchemy models.
    """
    __tablename__ = 'readers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
Base.metadata.create_all(engine) # Sukurk lenteles jeigu ju nera

# book = Book(year=2009, title='Python Programming 0.5', author='John Doe')

# with session_maker() as session:
#     session.add(book)
#     session.commit()

# with session_maker() as session:
#     book = session.get(Book, 5)
#     print(book)

# from sqlalchemy import select
# with session_maker() as session:
#     stmt = select(Book).where(Book.year > 2000)
#     results = session.scalars(stmt).all()
#     for book in results:
#         print(book)

# with session_maker() as session:
#     stmt = select(Book).group_by(Book.year).order_by(Book.year)
#     results = session.scalars(stmt).all()
#     for book in results:
#         print(book)
        

# from sqlalchemy import select
# with session_maker() as session:
#     stmt = select(Book).where(or_(
#         Book.year > 2000,
#           Book.year < 2010
#           ))
#     results = session.scalars(stmt).all()
#     for book in results:
#         print(book)

# with session_maker() as session:
#     book = session.get(Book, 32)
#     if book:
#         print(book)
#         book.author = 'New Author'
#         session.commit()
#     else:
#         print("Book not found.")
with session_maker() as session:
    book = session.get(Book, 1)
    if book:
        print(book)
        session.delete(book)
        session.commit()
    else:
        print("Book not found.")
