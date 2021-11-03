import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie
from price_code import PriceCode
from datetime import date


class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""
	
	def setUp(self):
		"""Test fixture contains:
		
		c = a customer
		movies = list of some movies
		"""
		self.year = date.today().year
		self.customer = Customer("Movie Mogul")
		self.new_movie = Movie("Mulan", self.year)
		self.regular_movie = Movie("CitizenFour", 2010)
		self.childrens_movie = Movie("Frozen", 2016, ['Children'])
		
	@unittest.skip("No convenient way to test")
	def test_billing():
		# no convenient way to test billing since its buried in the statement() method.
		pass
	
	def test_statement(self):
		stmt = self.customer.statement()
		# visual testing
		print(stmt)
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.customer.add_rental(Rental(self.new_movie, 4)) # days
		stmt = self.customer.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])
