from faker import Faker
import random
from model import engine,session, Restaurant,Customer,Review


session.query(Restaurant).delete()
session.query(Customer).delete()
session.query(Review).delete()

fake = Faker()

# For Restaurants

RESTAURANTS =[]
for i in range (10):
    restaurant= Restaurant(
        name =fake.unique.company(),
        price = random.randint(1000,50000)
    )

    session.add (restaurant)
    session.commit()

RESTAURANTS.append(restaurant)

# For Customer

customers =[]
for i in range (10):
    customer = Customer(
        first_name = fake.first_name(),
        last_name = fake.last_name()
    )

    session.add (customer)
    session.commit()
    customers.append(customer)

# For Reviews

reviews = []
star_ratings = [0, 1, 2, 3, 4, 5]

for restaurant in RESTAURANTS:
    for i in range(random.randint(1,10)):
        customer = random.choice(customers)
    

        star_rating = random.choice(star_ratings)
        print(f"Star Rating: {star_rating}")

        review = Review(
                star_rating=star_rating,
                restaurant_id=restaurant.id,
                customer_id=customer.id
            )
        reviews.append(review)

# for review in reviews:
        session.add(review)


session.commit()
session.close()