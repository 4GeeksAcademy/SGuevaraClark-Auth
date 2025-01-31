from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    address = db.relationship('Addresses', backref='user', uselist= False) # esto devuelve un objeto

    def __repr__(self):
        return f'<Users {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
            "address": self.address.serialize() if self.address else None
        }
    

class Addresses(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'<Address {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
            "address": self.address
        }


class Authors(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(250), nullable=False)
    books = db.relationship('Books', backref='author', lazy= True)

    def __repr__(self):
        return f'<Authors {self.full_name}>'

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
            "full_name": self.full_name,
            "books": [book.serialize() for book in self.books] if self.books else None
        }
    

class Books_Categories(db.Model):
    __tablename__ = 'books_categories'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __repr__(self):
        return f'<Books_Categories {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
            "book_id": self.book_id,
            "category": self.category_id
        }


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable= False)
    book_categories = db.relationship('Books_Categories', backref='category', lazy=True)

    def __repr__(self):
        return f'<Books {self.title}>'

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
            "title": self.title
        }
    

class Categories(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(250), nullable=False)
    book_categories = db.relationship('Books_Categories', backref='books', lazy=True)

    def __repr__(self):
        return f'<Books {self.title}>'

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
            "title": self.title
        }