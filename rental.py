from movie import *
from price_code import PriceCode
import logging


class Rental:
    """ A rental of a movie by customer. From Fowler's refactoring example.
        A realistic Rental would have fields for the dates that the movie was rented and returned, from which the
        rental period is calculated. But for simplicity of the example only a days_rented field is used."""

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
        a movie with known rental period (daysRented). """
        self.movie = movie
        self.price_code = PriceCode.for_movie(self.movie)
        if not isinstance(self.price_code, PriceCode):
            log = logging.getLogger()
            log.error(f"Movie {self.movie.get_movie_title()} has unrecognized priceCode {self.movie}")
        self.days_rented = days_rented

    def get_movie_title(self):
        return self.movie.get_title()

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        return self.price_code.price(self.get_days_rented())

    def get_point(self):
        return self.price_code.points(self.get_days_rented())
