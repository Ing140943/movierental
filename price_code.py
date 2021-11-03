from enum import Enum
from movie import Movie
from datetime import date


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0 * days,
                   "frp": lambda days: days}
    normal = {"price": lambda days: 2.0 if days <= 2 else 2.0 + (1.5 * (days-2)),
              "frp": lambda days: 1}
    childrens = {"price": lambda days: 1.5 if days <= 3 else 1.5 + (1.5 * (days-3)),
                 "frp": lambda days: 1}

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days"""
        pricing = self.value["price"]  # the enum member's price formula
        return pricing(days)

    def points(self, days: int) -> float:
        """Return the rental points for a given of days of new release movie or regular movie."""
        point = self.value["frp"]
        return point(days)

    @classmethod
    def for_movie(cls, movie: Movie):
        year = date.today().year
        if year == movie.get_year():
            return cls.new_release
        elif movie.get_genre('Children'):
            return cls.childrens
        else:
            return cls.normal
