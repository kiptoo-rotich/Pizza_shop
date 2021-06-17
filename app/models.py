from . import db
from . import login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin,db.Model):
    '''
    '''
    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    password_secure=db.Column(db.String(255))
    location=db.Column(db.String(255))
    shopping=db.relationship('Shopping',backref="shoppings",lazy="dynamic")
    order=db.relationship('Order',backref="orders" ,lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password atribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
    
    def verify_password(self,password):
        self.check_password_hash(self.password_secure,password)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return f'{self.username}'
    
class Order(db.Model):
    '''
    '''
    __tablename__="order"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    shopping=db.relationship("Shopping",backref="shopping",lazy="dynamic")
    order_date=db.Column(db.DateTime,default=datetime.utcnow)
    total_cost=db.Column(db.Integer())
    def save_order(self):
        db.session.add(self)
        db.session.commit()
    def add_order(self):
        orders=Order.query.filter().all()
        orders.save_order()
    @classmethod
    def get_order(cls,self):
        single_order=Order.query.filter_by(shoping_id=id).all()
    @classmethod
    def get_all_orders(cls,self):
        single_order=Order.query.filter_by(id).all()
        return single_order
    def __repr__(self):
        return f'{self.user_id}:{self.order_id}'
    
class Shopping(db.Model):
    '''
    '''
    __tablename__="shopping"
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    order_id=db.Column(db.Integer,db.ForeignKey("order.id"))
    pizza_category=db.Column(db.String(255))
    topping_category=db.Column(db.String(255))
    quantity=db.Column(db.Integer())
    cost=db.Column(db.Integer())
    def save_shopping(self):
        db.session.add(self)
        db.session.commit()
    def add_shopping(self):
        shopping=Shopping.query.filter_by(order_id=id).all()
        shopping.save_shopping()
    @classmethod
    def get_shopping(cls,self):
        new_shopping=Shopping.query.filter_by(id).all()
    @classmethod
    def get_all_shopping(cls,self):
        new_shopping=Shopping.query.filter_by().all()
        return new_shopping
    def __repr__(self):
        return f'{self.user_id}:{self.order_id}'