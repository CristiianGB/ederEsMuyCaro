from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#nombrevariable para hacer el relationship
favorites = db.Table("favorites", #nombre de la tabla
            db.Column("product_id", db.Integer, db.ForeignKey("product.product_id"), unique=False, nullable=False ),
            db.Column("user_id", db.Integer, db.ForeignKey("user.id"), unique=False, nullable=False )
        )               #nombre columna/tipo/relacion/atributosColumna
# nombre_de_objetos(variable) = db.Table('nombre de la tabla',
#     db.Column('nombre columna',tipo columna, db.ForeignKey("relacion modelo.columna"),atributos(unique,nullable)),
#     db.Column('nombre columna',tipo columna, db.ForeignKey("relacion modelo.columna"),atributos(unique,nullable)),
# )
class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    product = db.relationship('Product')
    product_quantity = db.Column(db.Integer, unique=False, nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"), unique=True, nullable=False )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=False, nullable=False )
    user = db.relationship('User')
    def serialize(self):
        return {
            "cart_id" : self.cart_id,
            "product_quantity":self.product_quantity,
            "cart_price": self.product.product_price*self.product_quantity,
            "product_id": self.product_id,
            "user_id": self.user_id
        }
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    first_name = db.Column(db.String(30), nullable=False, unique=False)
    last_name = db.Column(db.String(30), nullable=False, unique=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship('Product', secondary=favorites, lazy='subquery',
        backref=db.backref('favorites', lazy=True))

    def __repr__(self):
        return f'<User {self.email} >'

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name" : self.last_name,
            "email": self.email
 # do not serialize the password, its a security breach
        }
class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True, unique= True)
    product_name = db.Column(db.String(120), nullable=False, unique=False)
    product_price = db.Column(db.Integer, unique=False, nullable=False)
    
    def __repr__(self):
        return self.product_name

    def serialize(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "product_price": self.product_price
            }



