import os
import subprocess
from flask import Flask, jsonify, abort, render_template, redirect, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
import json
#import tests

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
from models import *

app.config.update(dict(
	DEBUG=True,
	SECRET_KEY = 'development key',
	USERNAME = 'admin',
	PASSWORD = 'default'
))
#app.config.from_envvar('PROJECT_SETTINGS', silent=True)

def init_db():
	db.drop_all()
	db.create_all()

def populate_db():
	session = db.create_scoped_session()
	f = open('SQL/insert_all.sql', 'r')
	for line in f:
		session.execute(line)
	f.close()
	session.commit()
	#f = open('SQL/job_data_insert.sql', 'r')
	#for line in f:
	#	session.execute(line)
	#f.close()
	#session.commit()

# Loading JSON from files. To be replaced with database or model calls
'''
f = open('Job.json') 
jobs = json.load(f)
f.close()

f = open('Company.json')
companies = json.load(f)
f.close()

f = open('Location.json')
locations = json.load(f)
f.close()

f = open('Language.json')
languages = json.load(f)
f.close()

f = open('Skillset.json')
skillsets = json.load(f)
f.close()

f = open('Member.json')
members = json.load(f)
f.close()
'''

# The following are examples of different templates in action
@app.route('/')
def root():
	return redirect('http://104.130.229.90:5000/index', code=302)
	#return redirect('http://127.0.0.1:5000/index', code=302)

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/tests')
def test():
	return render_template('tests.html')

@app.route('/result')
def result():
	with open('testresult.txt', 'w') as output:
	    p = subprocess.Popen(['python', 'tests.py'], stderr=output)
	    p.communicate()[0]
	output.close()

	with open('testresult.txt', 'r') as output:
	    outputStr = output.readlines()

	return render_template('result.html', result=outputStr)


# API
@app.route('/api/job', methods=['GET'])
def get_jobs():
	jobs = Job.query.all()
	return jsonify(Jobs = [job.serialize() for job in jobs])

@app.route('/api/job/<int:job_id>', methods=['GET'])
def get_job(job_id):
	job = Job.query.get(job_id)
	if not job:
		abort(jsonify({"error": "Item does not exist"}))
	return jsonify(job.serialize())

@app.route('/api/company', methods=['GET'])
def get_companies():
	companies = Company.query.all()
	return jsonify(Companies = [comEle.serialize() for comEle in companies])
		
@app.route('/api/company/<int:company_id>', methods=['GET'])
def get_company(company_id):
	company = Company.query.get(company_id)
	if not company:
		abort(jsonify({"error": "Item does not exist"}))
	return jsonify(company.serialize())

@app.route('/api/location', methods=['GET'])
def get_locations():
	locations = Location.query.all()
	return jsonify(locations = [locEle.serialize() for locEle in locations])

@app.route('/api/location/<int:location_id>', methods=['GET'])
def get_location(location_id):
	location = Location.query.get(location_id)
	if not location:
		abort(jsonify({"error": "Item does not exist"}))
	return jsonify(location.serialize())
	
#Member
@app.route('/api/member', methods=['GET'])
def get_team_member():
	member = Member.query.all()
	return jsonify(Members = [memEle.serialize() for memEle in member])
	

@app.route('/api/language', methods=['GET'])
def get_languages():
	languages = Language.query.all()
	return jsonify(languages = [langEle.serialize() for langEle in languages])

@app.route('/api/language/<int:language_id>', methods=['GET'])
def get_language(language_id):
	language = Language.query.get(language_id)
	if not language:
		abort(jsonify({"error": "Item does not exist"}))
	return jsonify(language.serialize())

@app.route('/api/skillset', methods=['GET'])
def get_skillsets():
	skillsets = Skillset.query.all()
	return jsonify(Skillsets = [skillset.serialize() for skillset in skillsets])

@app.route('/api/skillset/<int:skillset_id>', methods=['GET'])
def get_skillset(skillset_id):
	skillset = Skillset.query.get(skillset_id)
	if not skillset :
		abort(jsonify({"error": "Item does not exist"}))
	return jsonify(skillset.serialize())





#Dynamic pages
@app.route('/language')
def get_languages_page():
	languages = Language.query.all()
	return render_template('languages.html', langJson=languages)

@app.route('/language/<int:id>')
def get_language_page(id=None):
	language = Language.query.get(id)
	languages = Language.query.all()
	jobs = Job.query.all()
	companies = Company.query.all()
	locations = Location.query.all()
	skillsets = Skillset.query.all()
	
	return render_template('language.html', langJson=language, langsJson=languages, cmpyJson=companies, jobJson=jobs, locJson=locations, skillsetJson=skillsets)

@app.route('/location')
def get_locations_page():
	locations = Location.query.all()
	companies = Company.query.all()
	languages = Language.query.all()
	return render_template('locations.html', langJson=languages, cmpyJson=companies, locJson=locations)

@app.route('/location/<int:id>')
def get_location_page(id=None):
	#location = [location for location in locations if location['location_name'] == name]
	#location = location[0]
	location = Location.query.get(id)
	languages = Language.query.all()
	jobs = Job.query.all()
	companies = Company.query.all()
	locations = Location.query.all()
	skillsets = Skillset.query.all()
	return render_template('location.html', locJson = location, langJson=languages, cmpyJson=companies, locsJson=locations, jobJson=jobs, skillsetJson=skillsets)

@app.route('/skillset/<int:id>')
def get_skillset_page(id=None):
	skillset = Skillset.query.get(id)
	languages = Language.query.all()
	jobs = Job.query.all()
	companies = Company.query.all()
	locations = Location.query.all()
	skillsets = Skillset.query.all()
	#skillset = [skillset for skillset in skillsets if skillset['skillset_name'] == name]
	#skillset = skillset[0]
	return render_template('skillset.html', skillsetJson=skillset, jobJson=jobs, locJson=locations, cmpyJson=companies, langJson=languages)

@app.route('/job/<int:id>')
def get_job_page(id=None):
	job = Job.query.get(id)
	languages = Language.query.all()
	jobs = Job.query.all()
	companies = Company.query.all()
	locations = Location.query.all()
	skillsets = Skillset.query.all()
	#job = [job for job in jobs if job['job_title'] == name]
	#job = job[0]
	return render_template('job.html', jobsJson=jobs,  jobJson=job, cmpyJson=companies, langJson=languages, locJson=locations, skillsetJson=skillsets)

@app.route('/company')
def get_companies_page():
	companies = Company.query.all()
	companies = Company.query.all()
	locations = Location.query.all()
	return render_template('companies.html',cmpyJson=companies)

@app.route('/company/<int:id>')
def get_company_page(id=None):
	company = Company.query.get(id)
	languages = Language.query.all()
	jobs = Job.query.all()
	companies = Company.query.all()
	locations = Location.query.all()
	skillsets = Skillset.query.all()
	return render_template('company.html', cmpyJson = company, cmpysJson = companies, locsJson=locations, langJson=languages, jobJson=jobs, skillsetJson=skillsets)

@app.route('/about')
def get_about_page():
	members = Member.query.all()
	return render_template('about.html', memJson=members)

@app.route('/modeldoc')
def get_model_doc_page():
	return send_from_directory('.', 'models.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
