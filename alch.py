from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Data/duombaze.db', echo=True)
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
Base.metadata.create_all(engine)

book = Book(title='1984', author='George Orwell', year=1949)

with session_maker() as session:
    session.add(book)
    session.commit()