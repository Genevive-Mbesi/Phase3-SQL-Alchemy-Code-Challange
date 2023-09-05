from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Restaurant, Review, Customer

# Create an SQLite database (you can replace 'sqlite:///your_database.db' with your preferred database URL).
engine = create_engine('sqlite:///restaurants.db')

# Create the tables in the database.
Base.metadata.create_all(engine)

# Create a session to interact with the database.
Session = sessionmaker(bind=engine)
session = Session()
print("________________RESTAURANT______________")
#create restaurant instance
restaurant1 = session.query(Restaurant).first()

# Access the reviews attribute directly, don't call it like a method
print("________get__reviews_____")
print(restaurant1.get_reviews())
@property
def get_reviews(self):
    query = session.query(Review).filter_by(id=self.id)
    return query

print("________get_customers_____")
@property
def get_customer(self):
    query = session.query(Customer).filter_by(id=self.id)
    for result in query:
        return result
    return None
print(restaurant1.get_customer())



print("________________REVIEW______________")
#create Review instance
review1 = session.query(Review).first()
print(review1.customer_id)


res1 = review1.get_customer()
res2 = review1.get_restaurant()

print(res1)
print(res2)


print("________________CUSTOMER______________")

customer1 =session.query(Customer).first()
print(customer1.get_reviews())
print(customer1.get_restaurants())




first_restaurant = session.query(Customer).first()

# Access the first review associated with the customer
first_review = first_restaurant.reviews[0]

# Access the restaurant associated with the review
first_customer = first_review.restaurant

print(first_customer)
