import unittest
from programmerJobs import app
from models import Job, Company, Location, Language, Skillset

import json
import requests
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

	def testAddCompany(self):
		content = (999,'a','as','asd','asdf')
		db.add(content)
		ad.commit(content)



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
	url =  "http://104.130.229.90:5000/api/"

	# testing the whole set of Language data.
	def test_lang(self):
		response = requests.get(self.url + "language")
		self.assertEqual(response.status_code, 200)
		content = response.json()
		# the whole dataset in the languages
		temp = {{
  "languages": [
    {
      "language_description": "Muti platiform Language", 
      "language_id": 1, 
      "language_image": "images/language_icon/java_icon.png", 
      "language_name": "Java", 
      "language_wiki_description": "Java is a general-purpose computer programming language that is concurrent, class-based, object-oriented, and specifically designed to have as few implementation dependencies as possible. It is intended to let application developers  write once, run anywhere  (WORA), meaning that compiled Java code can run on all platforms that support Java without the need for recompilation. Java applications are typically compiled to bytecode that can run on any Java virtual machine (JVM) regardless of computer architecture. As of 2015, Java is one of the most popular programming languages in use, particularly for client-server web applications, with a reported 9 million developers. Java was originally developed by James Gosling at Sun Microsystems (which has since merged into Oracle Corporation) and released in 1995 as a core component of Sun Microsystems  Java platform. The language derives much of its syntax from C and C++, but it has fewer low-level facilities than either of them.", 
      "language_wiki_link": "http://en.wikipedia.org/wiki/Java_%28programming_language%29"
    }, 
    {
      "language_description": "great Language", 
      "language_id": 2, 
      "language_image": "images/language_icon/cpp_icon.png", 
      "language_name": "C++", 
      "language_wiki_description": "C++ is a general-purpose programming language. It has imperative, object-oriented and generic programming features, while also providing the facilities for low-level memory manipulation.", 
      "language_wiki_link": "http://en.wikipedia.org/wiki/C%2B%2B"
    }, 
    {
      "language_description": "Web Language", 
      "language_id": 3, 
      "language_image": "images/language_icon/php_icon.png", 
      "language_name": "PHP", 
      "language_wiki_description": "PHP is a server-side scripting language designed for web development but also used as a general-purpose programming language. As of January 2013, PHP was installed on more than 240 million websites (39% of those sampled) and 2.1 million web servers. Originally created by Rasmus Lerdorf in 1994, the reference implementation of PHP (powered by the Zend Engine) is now produced by The PHP Group. While PHP originally stood for Personal Home Page, it now stands for PHP: Hypertext Preprocessor, which is a recursive backronym.", 
      "language_wiki_link": "http://en.wikipedia.org/wiki/PHP"
    }, 
    {
      "language_description": "simple Language", 
      "language_id": 4, 
      "language_image": "images/language_icon/python_icon.png", 
      "language_name": "Python", 
      "language_wiki_description": "Python is a widely used general-purpose, high-level programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than would be possible in languages such as C++ or Java. The language provides constructs intended to enable clear programs on both a small and large scale.", 
      "language_wiki_link": "http://en.wikipedia.org/wiki/Python_%28programming_language%29"
    }, 
    {
      "language_description": "web Language", 
      "language_id": 5, 
      "language_image": "images/language_icon/javascript_icon.png", 
      "language_name": "Javascript", 
      "language_wiki_description": "JavaScript is a dynamic computer programming language. It is most commonly used as part of web browsers, whose implementations allow client-side scripts to interact with the user, control the browser, communicate asynchronously, and alter the document content that is displayed. It is also used in server-side network programming with runtime environments such as Node.js, game development and the creation of desktop and mobile applications. With the rise of the single-page web app and JavaScript-heavy sites, it is increasingly being used as a compile target for source-to-source compilers from both dynamic languages and static languages.", 
      "language_wiki_link": "http://en.wikipedia.org/wiki/JavaScript"
    }, 
    {
      "language_description": "Apple Language", 
      "language_id": 6, 
      "language_image": "images/language_icon/objective-c_icon.png", 
      "language_name": "Objective-C", 
      "language_wiki_description": "Objective-C is a general-purpose, object-oriented programming language that adds Smalltalk-style messaging to the C programming language. It is the main programming language used by Apple for the OS X and iOS operating systems, and their respective application programming interfaces (APIs), Cocoa and Cocoa Touch.", 
      "language_wiki_link": "http://en.wikipedia.org/wiki/Objective-C"
    }, 
    {
      "language_description": "Microsoft Language", 
      "language_id": 7, 
      "language_image": "images/language_icon/csharp_icon.png", 
      "language_name": "CSharp", 
      "language_wiki_description": "C# is a multi-paradigm programming language encompassing strong typing, imperative, declarative, functional, generic, object-oriented (class-based), and component-oriented programming disciplines. It was developed by Microsoft within its  NET initiative and later approved as a standard by Ecma (ECMA-334) and ISO (ISO/IEC 23270:2006). C# is one of the programming languages designed for the Common Language Infrastructure.", 
      "language_wiki_link": "http://en.wikipedia.org/wiki/C_Sharp_(programming_language)"
    }, 
    {
      "language_description": "Microsoft Language", 
      "language_id": 8, 
      "language_image": "images/language_icon/vbnet_icon.png", 
      "language_name": "Visual Basic.NET", 
      "language_wiki_description": "Visual Basic  NET (VB.NET) is a multi-paradigm, high level programming language, implemented on the  NET Framework. Microsoft launched VB.NET in 2002 as the successor to its original Visual Basic language. Although the  NET portion was dropped in 2005, this article uses Visual Basic  NET to refer to all Visual Basic languages releases since 2002, in order to distinguish between them and the classic Visual Basic. Along with Visual C#, it is one of the two main languages targeting the  NET framework.", 
      "language_wiki_link": "http://en.wikipedia.org/wiki/Visual_Basic_.NET"
    }, 
    {
      "language_description": "Microsoft Language", 
      "language_id": 9, 
      "language_image": "images/language_icon/vb_icon.png", 
      "language_name": "Visual Basic", 
      "language_wiki_description": "Visual Basic is a third-generation event-driven programming language and integrated development environment (IDE) from Microsoft for its COM programming model first released in 1991. Microsoft intended Visual Basic to be relatively easy to learn and use. Visual Basic was derived from BASIC and enables the rapid application development (RAD) of graphical user interface (GUI) applications, access to databases using Data Access Objects, Remote Data Objects, or ActiveX Data Objects, and creation of ActiveX controls and objects.", 
      "language_wiki_link": "http://en.wikipedia.org/wiki/Visual_Basic"
    }, 
    {
      "language_description": "great Language", 
      "language_id": 10, 
      "language_image": "images/language_icon/c_icon.png", 
      "language_name": "C", 
      "language_wiki_description": "C is a general-purpose, imperative computer programming language. It supports structured programming, lexical variable scope and recursion, while a static type system prevents many unintended operations. By design, C provides constructs that map efficiently to typical machine instructions, and therefore it has found lasting use in applications that had formerly been coded in assembly language, including operating systems, as well as various application software for computers ranging from supercomputers to embedded systems.", 
      "language_wiki_link": "http://en.wikipedia.org/wiki/C_(programming_language)"
    }
  ]
}}
		self.assertTrue(content == temp)

	# testing a request to an individual language data
	def test_lang_id(self):
		response = requests.get(self.url + "language/1")
		self.assertEqual(response.status_code, 200)
		content = response.json()
		# the dataset of the language where id is 1
		temp = {{
  "langResult": [
    {
      "language_description": "Muti platiform Language", 
      "language_id": 1, 
      "language_image": "images/language_icon/java_icon.png", 
      "language_name": "Java", 
      "language_wiki_description": "Java is a general-purpose computer programming language that is concurrent, class-based, object-oriented, and specifically designed to have as few implementation dependencies as possible. It is intended to let application developers  write once, run anywhere  (WORA), meaning that compiled Java code can run on all platforms that support Java without the need for recompilation. Java applications are typically compiled to bytecode that can run on any Java virtual machine (JVM) regardless of computer architecture. As of 2015, Java is one of the most popular programming languages in use, particularly for client-server web applications, with a reported 9 million developers. Java was originally developed by James Gosling at Sun Microsystems (which has since merged into Oracle Corporation) and released in 1995 as a core component of Sun Microsystems  Java platform. The language derives much of its syntax from C and C++, but it has fewer low-level facilities than either of them.", 
      "language_wiki_link": "http://en.wikipedia.org/wiki/Java_%28programming_language%29"
    }
  ]
}}
		self.assertTrue(content == temp)

	# testing the request when the data is not available
	def test_lang_not_found(self):
		response = requests.get(self.url + "language/null")
		self.assertEqual(response.status_code, 404)


# Test companies
class CompanyApiTest(unittest.TestCase):

	# assuming we add our api onto our server
	url =  "http://104.130.229.90:5000/api/"

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
	url =  "http://104.130.229.90:5000/api/"

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
