from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.schema import ForeignKey


db = SQLAlchemy()

job_languages = db.Table('job_language',
	db.Column('job_id', db.Integer, db.ForeignKey('job.id')),
	db.Column('language_id', db.Integer, db.ForeignKey('language.Language_ID'))
)

job_skillsets = db.Table('job_skillset',
	db.Column('job_id', db.Integer, db.ForeignKey('job.id')),
	db.Column('skillset_id', db.Integer, db.ForeignKey('skillset.Skillset_ID'))
)

class Job(db.Model):
	""" 
	This is the Job model and has the following attributes:
	id (Integer) - A unique indentifier  
	title (Text) - Job title
	description (Text) - Job description
	link (Text) - URL of the job posting on the company's website
	locationid (Integer) - Identifier for the location of the job
	companyid (Integer) - Identifer for the company
	skillsetid (Integer) - Identifier for the skillset
	languageid (Integer) - Identifier for the programming language
	"""
	__tablename__ = 'job'
	#__table_args__ = {'useexisting': True}
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text)
	description = db.Column(db.Text)
	link = db.Column(db.Text)
	locationid = db.Column(db.Integer, ForeignKey('location.id'))
	companyid = db.Column(db.Integer, ForeignKey('company.id'))
	#languageid = db.Column(db.Integer, ForeignKey('language.id'))
	#skillsetid = db.Column(db.Integer, ForeignKey('skillset.id'))
	languages = db.relationship('Language', secondary=job_languages, backref='job', lazy='dynamic')
	skillsets = db.relationship('Skillset', secondary=job_skillsets, backref='job', lazy='dynamic')

	def __init__(self, title, locationID, companyID, description, link):
		self.title = title
		self.locationid = locationID
		self.companyid = companyID
		self.description = description
		self.link = link
	
	def __repr__(self):
		return '<Job %r>' % self.title

class Company(db.Model):
	"""
	This is the Company model and has the following attributes:
	Company_ID (Integer) - Unique identifier
	Company_Name (Text) - Name of the company
	Company_description (Text) - Description of the company 
	Company_image (Text) - URL for company image
	"""
	__tablename__ = 'company'
	#__table_args__ = {'useexisting': True}	
	
	Company_ID = db.Column(db.Integer, primary_key=True)
	Company_Name = db.Column(db.Text)
	Company_description = db.Column(db.Text)
	Company_image = db.Column(db.Text)

	def __init__(self, Company_Name, Company_description, Company_image):
		self.Company_Name = Company_Name
		self.Company_description = Company_description
		self.Company_image = Company_image
	
	def __repr__(self):
		return '<company %r>' % self.Company_Name

class Language(db.Model):
	"""
	This is the Language model and has the following attributes:
	Language_ID (Integer) - Unique identifier
	Language_Name (Text) - Name of the programming language
	Language_Description (Text) - Description of the programming language
	Language_Image (Text) - URL for the image of the programming language
	"""
	__tablename__ = 'language'        
	#__table_args__ = {'useexisting': True}

	Language_ID = db.Column(db.Integer, primary_key=True)
	Language_Name = db.Column(db.Text)
	Language_Description = db.Column(db.Text)
	Language_Image = db.Column(db.Text)

	def __init__(self, Language_Name, Language_Description, Language_Image):
		self.Language_Name = Language_Name
		self.Language_Description = Language_Description
		self.Language_Image = Language_Image
	
	def __repr__(self):
		return '<Language %r>' % self.Language_Name

class Location(db.Model):
	"""
	This is the Location model and has the following attributes:
	Location_ID (Integer) - Unique Identifier
	Location (Text) - Name of the location
	Location_description (Text) - Description of the location
	Location_image (Text) - URL for the location image
	"""
	__tablename__ = 'location'
	#__table_args__ = {'useexisting': True}

	Location_ID = db.Column(db.Integer, primary_key=True)
	Location = db.Column(db.Text)
	Location_description = db.Column(db.Text)
	Location_image = db.Column(db.Text)

	def __init__(self, Location, Location_description, Location_image):
		self.Location = Location
		self.Location_description = Location_description
		self.Location_image = Location_image

	def __repr__(self):
		return '<Location %r>' % self.Location

class Skillset(db.Model):
	"""
	This is the Skillset model and has the following attributes:
	Skillset_ID (Integer)  - Unique identifier
	Skillset (Text) - Name of the skillset
	Skillset_description (Text) - Description of the skillset
	"""
	__tablename__ = 'skillset'
	#__table_args__ = {'useexisting': True}

	Skillset_ID = db.Column(db.Integer, primary_key=True)
	Skillset = db.Column(db.Text)
	Skillset_description = db.Column(db.Text)

	def __init__(self, Skillset, Skillset_description):
		self.Skillset = Skillset
		self.Skillset_description = Skillset_description
	
	def __repr__(self):
		return '<Skillset %r>' % self.Skillset
