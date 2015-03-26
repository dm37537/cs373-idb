from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.schema import ForeignKey
from programmerJobs import db

class Job(db.Model):
	__tablename__ = 'job'
	__table_args__ = {'useexisting': True}
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	title = db.Column(db.Text, nullable=False)
	description = db.Column(db.Text)
        link = db.Column(db.Text)
	locationid = db.Column(db.Integer, ForeignKey('location.id'))
	companyid = db.Column(db.Integer, ForeignKey('company.id'))
	languageid = db.Column(db.Integer, ForeignKey('language.id'))
	skillsetid = db.Column(db.Integer, ForeignKey('skillset.id'))

	def __init__(self, title, locationID, companyID, languageID, skillsetID, description, link):
		self.title = title
		self.locationid = locationID
		self.companyid = companyID
		self.languageid = languageID
		self.skillsetid = skillsetID
		self.description = description
		self.link = link
	
	def __repr__(self):
		return '<Job %r>' % self.title

class Company(db.Model):
	__tablename__ = 'company'
        __table_args__ = {'useexisting': True}	
	
	Company_ID = db.Column(db.Integer, primary_key=True)
	Company_Name = db.Column(db.String(120))
	Company_description = db.Column(db.String(120))
	Company_image = db.Column(db.String(120))

	def __init__(self, Company_Name, Company_description, Company_image):
		self.Company_Name = Company_Name
		self.Company_description = Company_description
		self.Company_image = Company_image
	
	def __repr__(self):
		return '<company %r>' % self.Company_Name

class Language(db.Model):
	__tablename__ = 'language'        
	__table_args__ = {'useexisting': True}

	Language_ID = db.Column(db.Integer, primary_key=True)
	Language_Name = db.Column(db.String(4000))
	Language_Description = db.Column(db.String(4000))
	Language_Image = db.Column(db.String(4000))

	def __init__(self, Language_Name, Language_Description, Language_Image):
		self.Language_Name = Language_Name
		self.Language_Description = Language_Description
		self.Language_Image = Language_Image
	
	def __repr__(self):
		return '<Language %r>' % self.Language_Name

class Location(db.Model):
	__tablename__ = 'location'
        __table_args__ = {'useexisting': True}

	Location_ID = db.Column(db.Integer, primary_key=True)
	Location = db.Column(db.String(120))
	Location_description = db.Column(db.String(120))
	Location_image = db.Column(db.String(120))

	def __init__(self, Location, Location_description, Location_image):
		self.Location = Location
		self.Location_description = Location_description
		self.Location_image = Location_image

	def __repr__(self):
		return '<Location %r>' % self.Location

class Skillset:
	__tablename__ = 'skillset'
        __table_args__ = {'useexisting': True}

	Skillset_ID = db.Column(db.Integer, primary_key=True)
	Skillset = db.Column(db.String(120))
	Skillset_description = db.Column(db.String(120))

	def __init__(self, Skillset, Skillset_description):
		self.Skillset = Skillset
		self.Skillset_description = Skillset_description
	
	def __repr__(self):
		return '<Location %r>' % self.Skillset
