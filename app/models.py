from . import db

class User(db.Model):
    '''
    '''
    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    password=db.Column(db.String(255))
    location=db.Column(db.String(255))
    shopping=db.relationship('Shopping',backref="shoppings",lazy="dynamic")
    order=db.relationship('Order',backref="orders" ,lazy="dynamic")
class Order(db.Model):
    '''
    '''
    __tablename__="order"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    shopping=db.relatioship("Shopping",backref="shopping",lazy="dynamic")
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
    __tablenmae__="shoping"
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,ForeignKey("user.id"))
    order_id=db.Column(db.Integer,ForeignKey("order.id"))
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