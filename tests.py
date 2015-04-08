import unittest
from programmerJobs import app
from models import Job, Company, Location, Language, Skillset

import json
import requests
import os

class ProgrammerJobsTestCase(unittest.TestCase):
	
	def testCreatingJob(self):
		job = Job('Software Developer', 1, 1, 'Clickity-Clackity', 'www.google.com')
		assert job.job_title == 'Software Developer'
		assert job.location_ID == 1
		assert job.company_ID == 1
		assert job.job_description == 'Clickity-Clackity'
		assert job.link == 'www.google.com'

	def testModifyingJob(self):
		job = Job('Software Developer', 1, 1, 'Clickity-Clackity', 'www.google.com')
		job.job_title = 'Security Engineer'
		job.location_ID = 0
		job.company_ID = 0
		job.job_description = 'leet h4xxor'
		job.link = 'www.vir.us'
		assert job.job_title == 'Security Engineer'
		assert job.location_ID == 0
		assert job.company_ID == 0
		assert job.job_description == 'leet h4xxor'
		assert job.link == 'www.vir.us'

	def testModifyingJob2(self):
		job = Job('Software Developer', 1, 1, 'Clickity-Clackity', 'www.google.com')
		job.job_title = 'CEO'
		job.location_ID = 0
		job.company_ID = 0
		job.job_description = 'Top dog'
		job.link = 'www.google.com'
		assert job.job_title == 'CEO'
		assert job.location_ID == 0
		assert job.company_ID == 0
		assert job.job_description == 'Top dog'
		assert job.link == 'www.google.com'

	def testCreatingCompany(self):
		company = Company('elgooG', 'enigne hcraeS', 'gpj.elgooG', 'www.elgoog.com')
		assert company.company_name == 'elgooG'
		assert company.company_description == 'enigne hcraeS'
		assert company.company_image == 'gpj.elgooG'
		assert company.company_site == 'www.elgoog.com'

	def testModifyingCompany(self):
		company = Company('elgooG', 'enigne hcraeS', 'gpj.elgooG', 'www.elgoog.com')
		company.company_name = 'bing'
		company.company_description = 'not google'
		company.company_image = 'bell.png'
		company.company_site = 'www.bing.com'
		assert company.company_name == 'bing'
		assert company.company_description == 'not google'
		assert company.company_image == 'bell.png'
		assert company.company_site == 'www.bing.com'
	
	def testModifyingCompany2(self):
		company = Company('elgooG', 'enigne hcraeS', 'gpj.elgooG', 'www.elgoog.com')
		company.company_name = 'facebook'
		company.company_description = 'social network'
		company.company_image = 'blue.png'
		company.company_site = 'www.facebook.com'
		assert company.company_name == 'facebook'
		assert company.company_description == 'social network'
		assert company.company_image == 'blue.png'
		assert company.company_site == 'www.facebook.com'

	def testCreatingLocation(self):
		location = Location('Austin, TX', 'Live music capital of the world', 'austin.jpg')
		assert location.location_name == 'Austin, TX'
		assert location.location_description == 'Live music capital of the world'
		assert location.location_image == 'austin.jpg'

	def testModifyingLocation(self):
		location = Location('Austin', 'Live music capital of the world', 'austin.jpg')
		location.location_name = 'New York, New York'
		location.location_description = 'City that never sleeps'
		location.location_image = 'newyork.jpg'
		assert location.location_name == 'New York, New York'
		assert location.location_description == 'City that never sleeps'
		assert location.location_image == 'newyork.jpg'

	def testModifyingLocation2(self):
		location = Location('Austin, TX', 'Live music capital of the world', 'austin.jpg')
		location.location_name = 'San Francisco, CA'
		location.location_description = 'I\'ve been there'
		location.location_image = 'goldengatebridge.jpg'
		assert location.location_name == 'San Francisco, CA'
		assert location.location_description == 'I\'ve been there'
		assert location.location_image == 'goldengatebridge.jpg'
	
	def testCreatingLanguage(self):
		language = Language('Spanish', 'taco, burrito, ...', 'sombrero.png', 'large_sombrero.png')
		assert language.language_name == 'Spanish'
		assert language.language_description == 'taco, burrito, ...'
		assert language.language_image_small == 'sombrero.png'
		assert language.language_image_large == 'large_sombrero.png'

	def testModifyingLanguage(self):
		language = Language('Spanish', 'taco, burrito, ...', 'sombrero.png','large_sombrero.png')
		language.language_name = 'French'
		language.language_description = 'Croissant'
		language.language_image_small = 'crepe.jpg'
		language.language_image_large = 'large_crepe.jpg'
		assert language.language_name == 'French'
		assert language.language_description == 'Croissant'
		assert language.language_image_small == 'crepe.jpg'
		assert language.language_image_large == 'large_crepe.jpg'

	def testModifyingLanguage2(self):
		language = Language('Spanish', 'taco, burrito, ...', 'sombrero.png', 'large_sombrero.png')
		language.language_name = 'English'
		language.language_description = 'Spoken in the USA'
		language.language_image_small = 'merica.jpg'
		language.language_image_large = 'large_merica.jpg'
		assert language.language_name == 'English'
		assert language.language_description == 'Spoken in the USA'
		assert language.language_image_small == 'merica.jpg'
		assert language.language_image_large == 'large_merica.jpg'

	def testCreatingSkillset(self):
		skillset = Skillset('Mobile Computing', 'walking computers')
		assert skillset.skillset_name == 'Mobile Computing'
		assert skillset.skillset_description == 'walking computers'

	def testModifyingSkillset(self):
		skillset = Skillset('Mobile Computing', 'walking computers')
		skillset.skillset_name = 'Android'
		skillset.skillset_description = 'Lollipop'
		assert skillset.skillset_name == 'Android'
		assert skillset.skillset_description == 'Lollipop'

	def testModifyingSkillset2(self):
		skillset = Skillset('Mobile Computing', 'walking computers')
		skillset.skillset_name = 'IOS'
		skillset.skillset_description = 'ipad'
		assert skillset.skillset_name == 'IOS'
		assert skillset.skillset_description == 'ipad'

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


if __name__ == '__main__':
	unittest.main()
