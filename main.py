# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from price_code import PriceCode
from rental import Rental
from customer import Customer
from movie_catalog import MovieCatalog


def make_movies():

    movie_catalog = MovieCatalog()
    movies = [
        movie_catalog.get_movie("Mulan"),
        movie_catalog.get_movie("Almost Holy"),
        movie_catalog.get_movie("Weathering With You"),
        movie_catalog.get_movie("Deadpool"),
        movie_catalog.get_movie("Weathering With You")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
