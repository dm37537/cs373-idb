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
	location_ID = db.Column(db.Integer, ForeignKey('location.Location_ID'))
	company_ID = db.Column(db.Integer, ForeignKey('company.Company_ID'))
	
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
	language_image_small (Text) - URL for the smaller image of the programming language
	language_image_large (Text) - URL for the larger image of the programming language
	"""
	__tablename__ = 'language'        

	language_ID = db.Column(db.Integer, primary_key=True)
	language_name = db.Column(db.Text)
	language_description = db.Column(db.Text)
	language_image_small = db.Column(db.Text)
	language_image_large = db.Column(db.Text)

	def __init__(self, Language_Name, Language_Description, Language_Image_Small, Language_Image_Large):
		self.language_name = Language_Name
		self.language_description = Language_Description
		self.language_image_small = Language_Image_Small
		self.language_image_large = Language_Image_Large
	
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

	def __init__(self, Skillset, Skillset_description):
		self.skillset_name = Skillset
		self.skillset_description = Skillset_description
	
	def __repr__(self):
		return '<Skillset %r>' % self.skillset_name
