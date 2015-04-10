import unittest
import socket
default_timeout = 10
socket.setdefaulttimeout(default_timeout)

from programmerJobs import db, app, get_languages, get_language, get_companies, get_company, get_locations, get_location
from models import Job, Company, Location, Language, Skillset
import urllib2
import json
import os


class DatabaseTestCase(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///databaseTest'
		self.app = app.test_client()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	# def testAddCompany(self):
	# 	content = (999,'a','as','asd','asdf')
	# 	db.add(content)
	# 	ad.commit(content)

class ProgrammerJobsTestCase(unittest.TestCase):
	
	def testCreatingJob(self):
		job = Job(1,'Software Developer', 1, 1, 'Clickity-Clackity', 'www.google.com')
		assert job.job_title == 'Software Developer'
		assert job.location_id == 1
		assert job.company_id == 1
		assert job.job_description == 'Clickity-Clackity'
		assert job.link == 'www.google.com'

	def testModifyingJob(self):
		job = Job(1,'Software Developer', 1, 1, 'Clickity-Clackity', 'www.google.com')
		job.job_title = 'Security Engineer'
		job.location_id = 0
		job.company_id = 0
		job.job_description = 'leet h4xxor'
		job.link = 'www.vir.us'
		assert job.job_title == 'Security Engineer'
		assert job.location_id == 0
		assert job.company_id == 0
		assert job.job_description == 'leet h4xxor'
		assert job.link == 'www.vir.us'

	def testModifyingJob2(self):
		job = Job(1, 'Software Developer', 1, 1, 'Clickity-Clackity', 'www.google.com')
		job.job_title = 'CEO'
		job.location_id = 0
		job.company_id = 0
		job.job_description = 'Top dog'
		job.link = 'www.google.com'
		assert job.job_title == 'CEO'
		assert job.location_id == 0
		assert job.company_id == 0
		assert job.job_description == 'Top dog'
		assert job.link == 'www.google.com'

	def testCreatingCompany(self):
		company = Company(1,'elgooG', 'enigne hcraeS', 'gpj.elgooG', 'www.elgoog.com')
		assert company.company_name == 'elgooG'
		assert company.company_description == 'enigne hcraeS'
		assert company.company_image == 'gpj.elgooG'
		assert company.company_site == 'www.elgoog.com'

	def testModifyingCompany(self):
		company = Company(1,'elgooG', 'enigne hcraeS', 'gpj.elgooG', 'www.elgoog.com')
		company.company_name = 'bing'
		company.company_description = 'not google'
		company.company_image = 'bell.png'
		company.company_site = 'www.bing.com'
		assert company.company_name == 'bing'
		assert company.company_description == 'not google'
		assert company.company_image == 'bell.png'
		assert company.company_site == 'www.bing.com'
	
	def testModifyingCompany2(self):
		company = Company(1,'elgooG', 'enigne hcraeS', 'gpj.elgooG', 'www.elgoog.com')
		company.company_name = 'facebook'
		company.company_description = 'social network'
		company.company_image = 'blue.png'
		company.company_site = 'www.facebook.com'
		assert company.company_name == 'facebook'
		assert company.company_description == 'social network'
		assert company.company_image == 'blue.png'
		assert company.company_site == 'www.facebook.com'

	def testCreatingLocation(self):
		location = Location(1,'Austin, TX', 'Live music capital of the world', 'austin.jpg')
		assert location.location_name == 'Austin, TX'
		assert location.location_description == 'Live music capital of the world'
		assert location.location_image == 'austin.jpg'

	def testModifyingLocation(self):
		location = Location(1,'Austin', 'Live music capital of the world', 'austin.jpg')
		location.location_name = 'New York, New York'
		location.location_description = 'City that never sleeps'
		location.location_image = 'newyork.jpg'
		assert location.location_name == 'New York, New York'
		assert location.location_description == 'City that never sleeps'
		assert location.location_image == 'newyork.jpg'

	def testModifyingLocation2(self):
		location = Location(1,'Austin, TX', 'Live music capital of the world', 'austin.jpg')
		location.location_name = 'San Francisco, CA'
		location.location_description = 'I\'ve been there'
		location.location_image = 'goldengatebridge.jpg'
		assert location.location_name == 'San Francisco, CA'
		assert location.location_description == 'I\'ve been there'
		assert location.location_image == 'goldengatebridge.jpg'
	
	def testCreatingLanguage(self):
		language = Language(1,'Spanish', 'taco, burrito, ...', 'sombrero.png', 'large_sombrero.png', 'image.jpg')
		assert language.language_name == 'Spanish'
		assert language.language_image == 'taco, burrito, ...'
		assert language.language_wiki_description == 'sombrero.png'
		assert language.language_description == 'large_sombrero.png'

	def testModifyingLanguage(self):
		language = Language(1,'Spanish', 'taco, burrito, ...', 'sombrero.png','large_sombrero.png', 'image.jpg')
		language.language_name = 'French'
		language.language_description = 'Croissant'
		language.language_image_small = 'crepe.jpg'
		language.language_image_large = 'large_crepe.jpg'
		assert language.language_name == 'French'
		assert language.language_description == 'Croissant'
		assert language.language_image_small == 'crepe.jpg'
		assert language.language_image_large == 'large_crepe.jpg'

	def testModifyingLanguage2(self):
		language = Language(1,'Spanish', 'taco, burrito, ...', 'sombrero.png', 'large_sombrero.png', 'image.jpg')
		language.language_name = 'English'
		language.language_description = 'Spoken in the USA'
		language.language_image_small = 'merica.jpg'
		language.language_image_large = 'large_merica.jpg'
		assert language.language_name == 'English'
		assert language.language_description == 'Spoken in the USA'
		assert language.language_image_small == 'merica.jpg'
		assert language.language_image_large == 'large_merica.jpg'

	def testCreatingSkillset(self):
		skillset = Skillset(1,'Mobile Computing', 'walking computers', 'image.jpg', 'wiki description', 'wiki.html')
		assert skillset.skillset_name == 'Mobile Computing'
		assert skillset.skillset_description == 'walking computers'

	def testModifyingSkillset(self):
		skillset = Skillset(1,'Mobile Computing', 'walking computers', 'image.jpg', 'wiki description', 'wiki.html')
		skillset.skillset_name = 'Android'
		skillset.skillset_description = 'Lollipop'
		assert skillset.skillset_name == 'Android'
		assert skillset.skillset_description == 'Lollipop'

	def testModifyingSkillset2(self):
		skillset = Skillset(1,'Mobile Computing', 'walking computers', 'image.jpg', 'wiki description', 'wiki.html')
		skillset.skillset_name = 'IOS'
		skillset.skillset_description = 'ipad'
		assert skillset.skillset_name == 'IOS'
		assert skillset.skillset_description == 'ipad'
"""
# change path in programmerjobs.py to 
# 	return redirect('http://127.0.0.1:5000/index', code=302)

# Test languages
class LanguageApiTest(unittest.TestCase):

	# assuming we add our api onto our server
	url =  "http://104.130.229.90:5000/api/"

	# testing the whole set of Language data.
	def test_lang(self):
		response = urllib2.urlopen('http://104.130.229.90:5000/api/language')
		self.assertEqual(response.code, 200)
		content = response.read()
		# the whole dataset in the languages
		temp = {}
		self.assertTrue(content == temp)

	# testing a request to an individual language data
	def test_lang_id(self):
		response = urllib2.urlopen('http://104.130.229.90:5000/api/language/1')
		self.assertEqual(response.status_code, 200)
		content = response.read()
		# the dataset of the language where id is 1
		temp = "null"
		self.assertTrue(content == temp)

	# testing the request when the data is not available
	def test_lang_not_found(self):
		response = urllib2.urlopen("http://104.130.229.90:5000/api/language/9000")
		self.assertEqual(response.status_code, 404)


# Test companies
class CompanyApiTest(unittest.TestCase):

	# assuming we add our api onto our server
	url =  "http://104.130.229.90:5000/api/"

	# testing the whole set of companies data.
	def test_company(self):
		response = urllib2.urlopen(url + 'company')
		self.assertEqual(response.status_code, 200)
		content = response.read()
		temp = '{\n  "Companies": [\n    {\n      "company_description": "Search engine", \n      "company_id": 1, \n      "company_image": "images/company_images/google_logo.png", \n      "company_name": "Google", \n      "company_site": "www.google.com"\n    }, \n    {\n      "company_description": "Database", \n      "company_id": 2, \n      "company_image": "images/company_images/oracle_logo.jpg", \n      "company_name": "Oracle", \n      "company_site": "www.oracle.com"\n    }, \n    {\n      "company_description": "Online shopping", \n      "company_id": 3, \n      "company_image": "images/company_images/amazon_logo.jpeg", \n      "company_name": "Amazon", \n      "company_site": "www.amazon.com"\n    }, \n    {\n      "company_description": "Social Media", \n      "company_id": 4, \n      "company_image": "images/company_images/facebook_logo.png", \n      "company_name": "Facebook", \n      "company_site": "www.facebook.com"\n    }, \n    {\n      "company_description": "Social Media", \n      "company_id": 5, \n      "company_image": "images/company_images/twitter_logo.png", \n      "company_name": "Twitter", \n      "company_site": "www.twitter.com"\n    }, \n    {\n      "company_description": "Online resume", \n      "company_id": 6, \n      "company_image": "images/company_images/linkedin_logo.png", \n      "company_name": "LinkedIn", \n      "company_site": "www.linkedin.com"\n    }, \n    {\n      "company_description": "computer", \n      "company_id": 7, \n      "company_image": "images/company_images/ibm_logo.jpg", \n      "company_name": "IBM", \n      "company_site": "www.ibm.com"\n    }, \n    {\n      "company_description": "Cloud service", \n      "company_id": 8, \n      "company_image": "images/company_images/dropbox_logo.png", \n      "company_name": "Dropbox", \n      "company_site": "www.dropbox.com"\n    }, \n    {\n      "company_description": "Cloud server provider", \n      "company_id": 9, \n      "company_image": "images/company_images/rackspace_logo.png", \n      "company_name": "Rackspace", \n      "company_site": "www.rackspace.com"\n    }, \n    {\n      "company_description": "Online yellow page for jobs", \n      "company_id": 10, \n      "company_image": "images/company_images/indeed_logo.png", \n      "company_name": "Indeed", \n      "company_site": "www.indeed.com"\n    }\n  ]\n}'# the whole dataset in the companies
		self.assertTrue(content == temp)

	# testing a request to an individual company data
	def test_company_id(self):
		response = urllib2.urlopen(url + 'company/1')
		self.assertEqual(response.status_code, 200)
		content = response.read()
		temp = '{\n  "company_description": "Search engine", \n  "company_id": 1, \n  "company_image": "images/company_images/google_logo.png", \n  "company_name": "Google", \n  "company_site": "www.google.com"\n}'# the dataset of the language where id is 1
		self.assertTrue(content == temp)

	# testing the request when the data is not available
	def test_company_not_found(self):
		response = urllib2.urlopen(url + 'company/9000')
		self.assertEqual(response.status_code, 404)


# Test locations
class LocationApiTest(unittest.TestCase):

	# assuming we add our api onto our server
	url =  "http://104.130.229.90:5000/api/"

	# testing the whole set of locations data.
	def test_location(self):
		response = urllib2.urlopen(url + 'location')
		self.assertEqual(response.status_code, 200)
		content = response.read()
		temp = {}# the whole dataset in the locations
		self.assertTrue(content == temp)

	# testing a request to an individual location data
	def test_location_id(self):
		response = urllib2.urlopen(url + 'location/1')
		self.assertEqual(response.status_code, 200)
		content = response.read()
		temp = {}# the dataset of the language where id is 1
		self.assertTrue(content == temp)

	# testing the request when the data is not available
	def test_location_not_found(self):
		response = urllib2.urlopen(url + 'location/9000')
		self.assertEqual(response.status_code, 404)
"""

if __name__ == '__main__':
	unittest.main()
