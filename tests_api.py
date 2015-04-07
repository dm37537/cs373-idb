import json
import requests
import os

# import TestCase
import unittest

# set os.environ[´´]



# Test languages
class LanguageApiTest(unittest.TestCase):

	# assuming we add our api onto our server
	url =  "http://  **put_our_URL_here**   /api/"

	# testing the whole set of Language data.
	def test_lang(self):
		response = requests.get(self.url + "languages/")
		self.assertEqual(response.status_code, 200)
		content = response.json()
		temp = # the whole dataset in the languages
		self.assertTrue(content == temp)

	# testing a request to an individual language data
	def test_lang_id(self):
		response = requests.get(self.url + "languages/1/")
		self.assertEqual(response.status_code, 200)
		content = response.json()
		temp = # the dataset of the language where id is 1
		self.assertTrue(content == temp)

	# testing the request when the data is not available
	def test_lang_not_found(self):
		response = requests.get(self.url + "languages/null/")
		self.assertEqual(response.status_code, 404)


# Test companies
class CompanyApiTest(unittest.TestCase):

	# assuming we add our api onto our server
	url =  "http://  **put_our_URL_here**   /api/"

	# testing the whole set of companies data.
	def test_company(self):
		response = requests.get(self.url + "companies/")
		self.assertEqual(response.status_code, 200)
		content = response.json()
		temp = # the whole dataset in the companies
		self.assertTrue(content == temp)

	# testing a request to an individual company data
	def test_company_id(self):
		response = requests.get(self.url + "companies/1/")
		self.assertEqual(response.status_code, 200)
		content = response.json()
		temp = # the dataset of the language where id is 1
		self.assertTrue(content == temp)

	# testing the request when the data is not available
	def test_company_not_found(self):
		response = requests.get(self.url + "companies/null/")
		self.assertEqual(response.status_code, 404)


# Test locations
class LocationApiTest(unittest.TestCase):

	# assuming we add our api onto our server
	url =  "http://  **put_our_URL_here**   /api/"

	# testing the whole set of locations data.
	def test_location(self):
		response = requests.get(self.url + "locations/")
		self.assertEqual(response.status_code, 200)
		content = response.json()
		temp = # the whole dataset in the locations
		self.assertTrue(content == temp)

	# testing a request to an individual location data
	def test_location_id(self):
		response = requests.get(self.url + "locations/1/")
		self.assertEqual(response.status_code, 200)
		content = response.json()
		temp = # the dataset of the language where id is 1
		self.assertTrue(content == temp)

	# testing the request when the data is not available
	def test_location_not_found(self):
		response = requests.get(self.url + "locations/null/")
		self.assertEqual(response.status_code, 404)