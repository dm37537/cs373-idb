import unittest
from programmerJobs import app
from models import Job, Company, Location, Language, Skillset

class ProgrammerJobsTestCase(unittest.TestCase):
	
	def testCreatingJob(self):
		job = Job('Software Developer', 1, 1, 1, 1, 'Clickity-Clackity', 'www.google.com')
		assert job.title == 'Software Developer'
		assert job.locationid == 1
		assert job.companyid == 1
		assert job.languageid == 1
		assert job.skillsetid == 1
		assert job.description == 'Clickity-Clackity'
		assert job.link == 'www.google.com'

	def testModifyingJob(self):
		job = Job('Software Developer', 1, 1, 1, 1, 'Clickity-Clackity', 'www.google.com')
		job.title = 'Security Engineer'
		job.locationid = 0
		job.companyid = 0
		job.languageid = 0
		job.skillsetid = 0
		job.description = 'leet h4xxor'
		job.link = 'www.vir.us'
		assert job.title == 'Security Engineer'
		assert job.locationid == 0
		assert job.companyid == 0
		assert job.languageid == 0
		assert job.skillsetid == 0
		assert job.description == 'leet h4xxor'
		assert job.link == 'www.vir.us'

	def testModifyingJob2(self):
		job = Job('Software Developer', 1, 1, 1, 1, 'Clickity-Clackity', 'www.google.com')
		job.title = 'CEO'
		job.locationid = 0
		job.companyid = 0
		job.languageid = 0
		job.skillsetid = 0
		job.description = 'Top dog'
		job.link = 'www.google.com'
		assert job.title == 'CEO'
		assert job.locationid == 0
		assert job.companyid == 0
		assert job.languageid == 0
		assert job.skillsetid == 0
		assert job.description == 'Top dog'
	    assert job.link == 'www.google.com'

	def testCreatingCompany(self):
		company = Company('elgooG', 'enigne hcraeS', 'gpj.elgooG')
		assert company.Company_Name == 'elgooG'
		assert company.Company_description == 'enigne hcraeS'
		assert company.Company_image == 'gpj.elgooG'

	def testModifyingCompany(self):
		company = Company('elgooG', 'enigne hcraeS', 'gpj.elgooG')
		company.Company_Name = 'bing'
		company.Company_description = 'not google'
		company.Company_image = 'bell.png'
		assert company.Company_Name == 'bing'
		assert company.Company_description == 'not google'
		assert company.Company_image == 'bell.png'

	def testModifyingCompany2(self):
		company = Company('elgooG', 'enigne hcraeS', 'gpj.elgooG')
		company.Company_Name = 'facebook'
		company.Company_description = 'social network'
		company.Company_image = 'blue.png'
		assert company.Company_Name == 'facebook'
		assert company.Company_description == 'social network'
		assert company.Company_image == 'blue.png'

	def testCreatingLocation(self):
		location = Location('Austin, TX', 'Live music capital of the world', 'austin.jpg')
		assert location.Location == 'Austin, TX'
		assert location.Location_description == 'Live music capital of the world'
		assert location.Location_image == 'austin.jpg'

	def testModifyingLocation(self):
		location = Location('Austin', 'Live music capital of the world', 'austin.jpg')
		location.Location = 'New York, New York'
		location.Location_description = 'City that never sleeps'
		location.Location_image = 'newyork.jpg'
		assert location.Location == 'New York, New York'
		assert location.Location_description == 'City that never sleeps'
		assert location.Location_image == 'newyork.jpg'

	def testModifyingLocation2(self):
		location = Location('Austin, TX', 'Live music capital of the world', 'austin.jpg')
		location.Location = 'San Francisco, CA'
		location.Location_description = 'I\'ve been there'
		location.Location_image = 'goldengatebridge.jpg'
		assert location.Location == 'San Francisco, CA'
		assert location.Location_description == 'I\'ve been there'
		assert location.Location_image == 'goldengatebridge.jpg'

	def testCreatingLanguage(self):
		language = Language('Spanish', 'taco, burrito, ...', 'sombrero.png')
		assert language.Language_Name == 'Spanish'
		assert language.Language_Description == 'taco, burrito, ...'
		assert language.Language_Image == 'sombrero.png'

	def testModifyingLanguage(self):
		language = Language('Spanish', 'taco, burrito, ...', 'sombrero.png')
		language.Language_Name = 'French'
		language.Language_Description = 'Croissant'
		language.Language_Image = 'crepe.jpg'
		assert language.Language_Name == 'French'
		assert language.Language_Description == 'Croissant'
		assert language.Language_Image == 'crepe.jpg'

	def testModifyingLanguage2(self):
		language = Language('Spanish', 'taco, burrito, ...', 'sombrero.png')
		language.Language_Name = 'English'
		language.Language_Description = 'Spoken in the USA'
		language.Language_Image = 'merica.jpg'
		assert language.Language_Name == 'English'
		assert language.Language_Description == 'Spoken in the USA'
		assert language.Language_Image == 'merica.jpg'

	def testCreatingSkillset(self):
		skillset = Skillset('Mobile Computing', 'walking computers')
		assert skillset.Skillset == 'Mobile Computing'
		assert skillset.Skillset_description == 'walking computers'

	def testModifyingSkillset(self):
		skillset = Skillset('Mobile Computing', 'walking computers')
		skillset.Skillset = 'Android'
		skillset.Skillset_description = 'Lollipop'
		assert skillset.Skillset == 'Android'
		assert skillset.Skillset_description == 'Lollipop'

	def testModifyingSkillset2(self):
		skillset = Skillset('Mobile Computing', 'walking computers')
		skillset.Skillset = 'IOS'
		skillset.Skillset_description = 'ipad'
		assert skillset.Skillset == 'IOS'
		assert skillset.Skillset_description == 'ipad'

'''
if __name__ == '__main__':
	unittest.main()
'''

def run():
	unittest.main()

run()