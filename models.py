from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.schema import ForeignKey
from programmerJobs import db

job_languages = db.Table('job_language',
	db.Column('job_ID', db.Integer, db.ForeignKey('job.job_ID')),
	db.Column('language_ID', db.Integer, db.ForeignKey('language.language_ID'))
)
job_skillsets = db.Table('job_skillset',
	db.Column('job_ID', db.Integer, db.ForeignKey('job.job_ID')),
	db.Column('skillset_ID', db.Integer, db.ForeignKey('skillset.skillset_ID'))
)

class Job(db.Model):
	""" 
	This is the Job model and has the following attributes:
	job_ID (Integer) - A unique indentifier  
	job_title (Text) - Job title
	job_description (Text) - Job description
	link (Text) - URL of the job posting on the company's website
	locationid (Integer) - Identifier for the location of the job
	companyid (Integer) - Identifer for the company
	skillsets (Iterable) - Iterable of skillsets needed for job
	languages (Iterable) - Iterable of languages needed for job
	"""
	__tablename__ = 'job'
	
	job_ID = db.Column(db.Integer, primary_key=True)
	job_title = db.Column(db.Text)
	job_description = db.Column(db.Text)
	link = db.Column(db.Text)
	location_ID = db.Column(db.Integer, ForeignKey('location.location_ID'))
	company_ID = db.Column(db.Integer, ForeignKey('company.company_ID'))
	
	languages = db.relationship('Language', secondary=job_languages, backref='job', lazy='dynamic')
	skillsets = db.relationship('Skillset', secondary=job_skillsets, backref='job', lazy='dynamic')

	def __init__(self, title, locationID, companyID, description, link):
		self.job_title = title
		self.location_ID = locationID
		self.company_ID = companyID
		self.job_description = description
		self.link = link
	
	def __repr__(self):
		return '<Job %r>' % self.job_title

class Company(db.Model):
	"""
	This is the Company model and has the following attributes:
	company_ID (Integer) - Unique identifier
	company_name (Text) - Name of the company
	company_description (Text) - Description of the company 
	company_image (Text) - URL for company image
	company_site (Text) - URL for company
	"""
	__tablename__ = 'company'
	
	company_ID = db.Column(db.Integer, primary_key=True)
	company_name = db.Column(db.Text)
	company_description = db.Column(db.Text)
	company_image = db.Column(db.Text)
	company_site = db.Column(db.Text)

	def __init__(self, Company_Name, Company_description, Company_image, Company_site):
		self.company_name = Company_Name
		self.company_description = Company_description
		self.company_image = Company_image
		self.company_site = Company_site
	
	def __repr__(self):
		return '<company %r>' % self.company_name

class Language(db.Model):
	"""
	This is the Language model and has the following attributes:
	language_ID (Integer) - Unique identifier
	language_name (Text) - Name of the programming language
	language_description (Text) - Description of the programming language
	language_wiki_description (Text) - URL for the smaller image of the programming language
	language_wiki_link (Text) - URL for the larger image of the programming language
	"""
	__tablename__ = 'language'        

	language_ID = db.Column(db.Integer, primary_key=True)
	language_name = db.Column(db.Text)
	language_image = db.Column(db.Text)
	language_description = db.Column(db.Text)
	language_wiki_link = db.Column(db.Text)

	def __init__(self, Language_Name, Language_Image, Language_Description, language_Wiki_link):
		self.language_name = Language_Name
		self.language_image = Language_Image
		self.language_description = Language_Description
		self.language_wiki_link = Language_Wiki_Link
	
	def serialize(self):
		#return dict
		return {
			'language_ID' : self.language_ID,
			'language_name' : self.language_name,
			'language_image' : self.language_image,
			'language_description' : self.language_description,
			'language_wiki_link' : self.language_wiki_link
			}

	def __repr__(self):
		return '<Language %r>' % self.language_name

class Location(db.Model):
	"""
	This is the Location model and has the following attributes:
	location_ID (Integer) - Unique Identifier
	location_name (Text) - Name of the location
	location_description (Text) - Description of the location
	location_image (Text) - URL for the location image
	"""
	__tablename__ = 'location'

	location_ID = db.Column(db.Integer, primary_key=True)
	location_name = db.Column(db.Text)
	location_description = db.Column(db.Text)
	location_image = db.Column(db.Text)

	def __init__(self, Location, Location_description, Location_image):
		self.location_name = Location
		self.location_description = Location_description
		self.location_image = Location_image

	def __repr__(self):
		return '<Location %r>' % self.location_name

class Skillset(db.Model):
	"""
	This is the Skillset model and has the following attributes:
	skillset_ID (Integer)  - Unique identifier
	skillset_name (Text) - Name of the skillset
	skillset_description (Text) - Description of the skillset
	"""
	__tablename__ = 'skillset'

	skillset_ID = db.Column(db.Integer, primary_key=True)
	skillset_name = db.Column(db.Text)
	skillset_description = db.Column(db.Text)
	skillset_image = db.Column(db.Text)
	skillset_wiki_description = db.Column(db.Text)
	skillset_wiki_link = db.Column(db.Text)

	def __init__(self, Skillset, Skillset_description, Skillset_image, Skillset_wiki_description, Skillset_wiki_link):
		self.skillset_name = Skillset
		self.skillset_description = Skillset_description
		self.skillset_image = Skillset_image
		self.skillset_wiki_description = Skillset_wiki_description
		self.skillset_wiki_link = Skillset_wiki_link

	
	def __repr__(self):
		return '<Skillset %r>' % self.skillset_name

class Member(db.Model):
	"""
	This is the Member model and has the following attributes:
	member_ID (Integer) - Unique identifier
	member_name (Text) - Name of a member
	member_bio (Text) - Biography for a member
	member_major_responsibility (Text) - Major responsibity for a member
	member_commit (Integer) - Number of commit 
	member_issue (Integer) - Number of issue
	member_unittest (Integer) - Number of unittest
	member_image (Text) - Image directory
	member_leader (Integer) - Number of leader
	"""

	__tablename__ = 'member'

	member_ID = db.Column(db.Integer, primary_key=True)
	member_name = db.Column(db.Text)
	member_bio = db.Column(db.Text)
	member_major_responsibility = db.Column(db.Text)
	member_commit = db.Column(db.Integer)
	member_issue = db.Column(db.Integer)
	member_unittest = db.Column(db.Integer)
	member_image = db.Column(db.Text)
	member_leader = db.Column(db.Integer)

	def __init__(self, Member_name, Member_bio, Member_major_responsibilit, Member_commit, Member_issue, Member_unittest, Member_image, Member_leader):
		self.member_name = Member_name
		self.member_bio = Member_bio
		self.member_major_responsibility = Member_major_responsibilit
		self.member_commit = Member_commit
		self.member_issue = Member_issue
		self.member_unittest = Member_unittest
		self.member_image = Member_image
		self.member_leader = Member_leader

	def __repr__(self):
		return '<Member %r>' % self.member_name
