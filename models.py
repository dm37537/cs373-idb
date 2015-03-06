from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db' #Change later
db = SQLAlchemy(app)

class Job(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(120))
	locationID = db.Column(db.Integer)
	companyID = db.Column(db.Integer)
	languageID = db.Column(db.Integer)
	skillsetID = db.Column(db.Integer) # ummmm model?
	description = db.Column(db.String(120)) # double check this against the API
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
	Company_ID = db.Column(db.Integer, primary_key=True)
	Company_Name = db.Column(db.String(80))
	Company_description = db.Column(db.String(120))
	Company_image = db.Column(db.String(120))

	def __init__(self, name, description, image):
		self.Company_Name = name
		self.Company_description = description
		self.image = image
	
	def __repr__(self):
		return '<Company %r>' % self.Company_Name

class Language(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	link = db.Column(db.String(120))
	image = db.Column(db.String(120))

	def __init__(self, name, link, image):
		self.name = name
		self.link = link
		self.image = image
	
	def __repr__(self):
		return '<Language %r>' % self.name
