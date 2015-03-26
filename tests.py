import unittest
from programmerJobs import app

class ProgrammerJobsTestCase(unittest.TestCase)
	
	def testCreatingJob(self):
		job = Job('Software Developer', 1, 1, 1, 1, 'Clickity-Clackity', 'www.google.com')
		assert job.title == 'Software Developer'
		assert job.locationID == 1
		assert job.companyID == 1
		assert job.languageID == 1
		assert job.skillsetID == 1
		assert job.description == 'Clickity-Clackity'
		assert job.link == 'www.google.com'
	
	def testModifyingJob(self):
		job = Job('Software Developer', 1, 1, 1, 1, 'Clickity-Clackity', 'www.google.com')
		job.title = 'Security Engineer'
		job.locationID = 0
		job.companyID = 0
		job.languageID = 0
		job.skillsetID = 0
		job.description = 'leet h4xxor'
		job.link = 'www.vir.us'
		assert job.id == 1
		assert job.title == 'Security Engineer'
		assert job.locationID == 0
		assert job.companyID == 0
		assert job.languageID == 0
		assert job.skillsetID == 0
		assert job.description == 'leet h4xxor'
		assert job.link == 'www.vir.us'

	
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
		assert location.Location_description = 'City that never sleeps'
		assert location.Location_image == 'newyork.jpg'
	
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
	
	def testCreatingSkillset(self):
		skillset = Skillset('Mobile Computing', 'walking computers')
		assert skillset.Skillset == 'Mobile Computing'
		assert skillset.Skillset_description == 'walking computers'
	
	def testModifyingSkillset(self):
		skillset = Skillset('Mobile Computing', 'walking computers')
		skillset.Skillset = 'Andriod'
		skillset.Skillset_description = 'Lollipop'
		assert skillset.Skillset == 'Android'
		assert skillset.Skillset_description == 'Lollipop'

if __name__ == '__main__':
	unittest.main()
