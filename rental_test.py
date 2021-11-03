import unittest

from customer import Customer
from movie_catalog import MovieCatalog
from rental import Rental
from movie import Movie
from price_code import PriceCode
from datetime import date


class RentalTest(unittest.TestCase):
	
	def setUp(self):

		self.year = date.today().year
		self.new_movie = Movie("Mulan", self.year)
		self.regular_movie = Movie("CitizenFour", 2010)
		self.childrens_movie = Movie("Frozen", 2016, ['Children'])
		self.catalog = MovieCatalog()

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		self.assertEqual("CitizenFour", self.regular_movie.get_title())
		self.assertEqual(2010, self.regular_movie.get_year())
		self.assertEqual(PriceCode.normal, PriceCode.for_movie(self.regular_movie))
		self.assertEqual("Mulan", self.new_movie.get_title())
		self.assertEqual(self.year, self.new_movie.get_year())
		self.assertEqual(PriceCode.new_release, PriceCode.for_movie(self.new_movie))
		self.assertEqual("Frozen", self.childrens_movie.get_title())
		self.assertEqual(2016, self.childrens_movie.get_year())
		self.assertEqual(PriceCode.childrens, PriceCode.for_movie(self.childrens_movie))

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental2 = Rental(self.regular_movie, 1)
		self.assertEqual(rental2.get_price(), 2.0)
		rental2 = Rental(self.regular_movie, 5)
		self.assertEqual(rental2.get_price(), 6.5)
		rental3 = Rental(self.childrens_movie, 1)
		self.assertEqual(rental3.get_price(), 1.5)
		rental3 = Rental(self.childrens_movie, 5)
		self.assertEqual(rental3.get_price(), 4.5)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_point(), 1.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_point(), 5.0)
		rental2 = Rental(self.regular_movie, 1)
		self.assertEqual(rental2.get_point(), 1.0)
		rental2 = Rental(self.regular_movie, 5)
		self.assertEqual(rental2.get_point(), 1.0)
		rental3 = Rental(self.childrens_movie, 1)
		self.assertEqual(rental3.get_point(), 1.0)
		rental3 = Rental(self.regular_movie, 5)
		self.assertEqual(rental3.get_point(), 1.0)
