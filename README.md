# Restaurant Review Domain

This application deals with a restaurant review domain and involves three models: `Restaurant`, `Review`, and `Customer`. It establishes relationships between these models and provides various methods to interact with them. Before you begin working on the methods, you should have set up the necessary database tables using SQLAlchemy migrations and populated them with seed data.

## Table of Contents
- [Migrations](#migrations)
- [Object Relationship Methods](#object-relationship-methods)
  - [Review](#review)
  - [Restaurant](#restaurant)
  - [Customer](#customer)
- [Aggregate and Relationship Methods](#aggregate-and-relationship-methods)
  - [Customer](#customer-1)
  - [Review](#review-1)
  - [Restaurant](#restaurant-1)
- [Contributors](#contributors)
- [Languages](#languages)
- [License](#license)

## Migrations

Before proceeding with the application's functionality, you need to create a migration for all necessary database tables, including the `reviews` table. The `reviews` table should have columns to establish relationships with `Restaurant` and `Customer` and include a `star_rating` column to store review ratings.

After creating the tables using migrations, use the `seeds.py` file to create sample instances of your classes for testing purposes.

## Object Relationship Methods

### Review
- `Review customer()`: Returns the `Customer` instance associated with this review.
- `Review restaurant()`: Returns the `Restaurant` instance associated with this review.

### Restaurant
- `Restaurant reviews()`: Returns a collection of all reviews for the restaurant.
- `Restaurant customers()`: Returns a collection of all customers who reviewed the restaurant.

### Customer
- `Customer reviews()`: Returns a collection of all reviews left by the customer.
- `Customer restaurants()`: Returns a collection of all restaurants reviewed by the customer.

Ensure that these methods work correctly by testing them in the console using your sample data.

## Aggregate and Relationship Methods

### Customer
- `Customer full_name()`: Returns the full name of the customer (first name and last name concatenated).
- `Customer favorite_restaurant()`: Returns the restaurant with the highest star rating from this customer.
- `Customer add_review(restaurant, rating)`: Adds a new review for the specified restaurant with the given rating.
- `Customer delete_reviews(restaurant)`: Removes all reviews by the customer for a specific restaurant.

### Review
- `Review full_review()`: Returns a formatted string with the review details, including restaurant name, customer's full name, and star rating.

### Restaurant
- `Restaurant fanciest() (class method)`: Returns the restaurant with the highest price.
- `Restaurant all_reviews()`: Returns a list of strings containing all reviews for the restaurant in a formatted manner.

Feel free to explore and test these methods to ensure they work as expected.

## Contributors

- [Genevive Mbesi](https://github.com/Genevive-Mbesi) - Provide a link to your GitHub profile if you contributed to this project.

## Languages

- Python - This project is primarily written in Python.

## License

This project is licensed under the [MIT License](LICENSE.md). See the [LICENSE.md](LICENSE.md) file for details.
