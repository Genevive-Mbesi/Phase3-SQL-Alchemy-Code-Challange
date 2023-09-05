from sqlalchemy import create_engine,func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine =create_engine('sqlite:///restaurants.db')

Session = sessionmaker (bind =engine)
session = Session ()

# Restaurant

class Restaurant(Base):
    __tablename__ ='restaurants'

    id = Column(Integer,primary_key= True)
    name = Column (String)
    price =Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')
    customers = association_proxy('reviews', 'customer', 
        creator = lambda cu: Review(customer = cu))

    def __repr__(self):
        return f'name = {self.name}, price = {self.price}'
    
    
    def get_reviews(self):
        query = session.query(Review).filter_by(id=self.id)
        for x in query:
            return x
        return None

    
    def get_customer(self):
        query = session.query(Customer).filter_by(id=self.id)
        for result in query:
            return result
        return None

# Customer
   
class Customer (Base):
    __tablename__ = 'customers'
     
    id = Column (Integer,primary_key=True)
    first_name =Column(String)
    last_name =Column(String)

    reviews = relationship('Review', back_populates='customer')
    customers = association_proxy('reviews', 'restaurant', 
        creator = lambda re: Review(restaurant = re))
    
    def get_reviews(self):
        query = session.query(Review).filter_by(customer_id = self.id)
        for cus in query:
            return cus
        return None
    
    def get_restaurants(self):
        query = session.query(Restaurant).filter_by(id = self.id)
        for cus in query:
            return cus
        return None
    
    def full_name(self):
        return f"{self.first_name}, {self.last_name}"
    


    def __repr__(self):
        return f'first_name = {self.first_name}, last_name = {self.last_name}' 
    
    
    # Review


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def __repr__(self):
        return f"id={self.id}, rating = {self.star_rating} customer={self.customer_id} for restaurant::{self.restaurant_id}"

    def get_customer(self):
        query = session.query(Customer).filter_by(id=self.customer_id).first()
        return query

    def get_restaurant(self):
        query = session.query(Restaurant).filter_by(id=self.restaurant_id).first()
        return query
    
    def full_review(self):
        return f"Review for '{self.restaurant.name} restaurant by {self.customer.full_name}: {self.star_rating} stars"

    

    




