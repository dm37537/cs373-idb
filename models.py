from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from programmerJobs import db

class Job(db.Model):
	__tablename__ = 'Job'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120))
	locationID = db.Column(db.Integer)
	companyID = db.Column(db.Integer)
	languageID = db.Column(db.Integer)
	skillsetID = db.Column(db.Integer)
	description = db.Column(db.String(120))
	link = db.Column(db.String(120))

	def __init__(self, title, locationID, companyID, languageID, skillsetID, description, link):
		self.title = title
		self.locationID = locationID
		self.companyID = companyID
		self.languageID = languageID
		self.skillsetID = skillsetID
		self.description = description
		self.link = link
	
	def __repr__(self):
		return '<Job %r>' % self.title

class Company(db.Model):
	__tablename__ = 'Company'

	Company_ID = db.Column(db.Integer, primary_key=True)
	Company_Name = db.Column(db.String(120))
	Company_description = db.Column(db.String(120))
	Company_image = db.Column(db.String(120))

	def __init__(self, Company_Name, Company_description, Company_image):
		self.Company_Name = Company_Name
		self.Company_description = Company_description
		self.image = Company_image
	
	def __repr__(self):
		return '<Company %r>' % self.Company_Name

class Language(db.Model):
	__tablename__ = 'Language'

	Language_ID = db.Column(db.Integer, primary_key=True)
	Language_Name = db.Column(db.String(120))
	Language_Description = db.Column(db.String(120))

	def __init__(self, Language_Name, Language_Description):
		self.Language_Name = Language_Name
		self.Language_Description = Language_Description
	
	def __repr__(self):
		return '<Language %r>' % self.Language_Name

class Location(db.Model):
	__tablename__ = 'Location'

	Location_ID = db.Column(db.Integer, primary_key=True)
	Location = db.Column(db.String(120))
	Location_description = db.Column(db.String(120))
	location_image = db.Column(db.String(120))

	def __init__(self, Location, Location_description, Location_image):
		self.Location = Location
		self.Location_description = Location_description
		self.Location_image = Location_image

	def __repr__(self):
		return '<Location %r>' % self.Location

class Skillset:
	__tablename__ = 'Skillset'

	Skillset_ID = db.Column(db.Integer, primary_key=True)
	Skillset = db.Column(db.String(120))
	Skillset_description = db.Column(db.String(120))

	def __init__(self, Skillset, Skillset_description):
		self.Skillset = Skillset
		self.Skillset_description = Skillset_description
	
	def __repr__(self):
		return '<Location %r>' % self.Skillset
