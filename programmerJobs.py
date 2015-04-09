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

# The following are examples of different templates in action
@app.route('/')
def root():
	return redirect('http://104.130.229.90:5000/index', code=302)

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/tests')
def test():
	# tests.run()
	return render_template('tests.html')
	# return send_from_directory('.', 'runTest.php

@app.route('/result')
def result():
	with open('testresult.txt', 'w') as output:
	    p = subprocess.Popen(['python', 'tests.py'], stderr=output)
	    p.communicate()[0]
	output.close()

	with open('testresult.txt', 'r') as output:
	    outputStr = output.readlines()

	return render_template('result.html', result=outputStr)

'''
# API
@app.route('/api/job', methods=['GET'])
def get_jobs():
	return jsonify({'jobs': jobs})

@app.route('/api/job/<int:job_id>', methods=['GET'])
def get_job(job_id):
	job = [job for job in jobs if job['job_ID'] == job_id]
	if len(job) == 0:
		abort(404)
	return jsonify({'job': job[0]})

@app.route('/api/company', methods=['GET'])
def get_companies():
	return jsonify({'companies': companies})
		
@app.route('/api/company/<int:company_id>', methods=['GET'])
def get_company(company_id):
	company = [company for company in companies if company['company_ID'] == company_id]
	if len(company) == 0:
		abort(404)
	return jsonify({'company': company[0]})

@app.route('/api/location', methods=['GET'])
def get_locations():
	return jsonify({'locations': locations})

@app.route('/api/location/<int:location_id>', methods=['GET'])
def get_location(location_id):
	location = [location for location in locations if location['location_ID'] == location_id]
	if len(location) == 0:
		abort(404)
	return jsonify({'location': location[0]})
	
#Member
@app.route('/api/member', methods=['GET'])
def get_team_member():
	return jsonify({'members': member})

@app.route('/api/language', methods=['GET'])
def get_languages():
	return jsonify({'languages': languages})

@app.route('/api/language/<int:language_id>', methods=['GET'])
def get_language(language_id):
	language = [language for language in languages if language['language_ID'] == language_id]
	if len(language) == 0:
		abort(404)
	return jsonify({'language': language[0]})

@app.route('/api/skillset', methods=['GET'])
def get_skillsets():
	return jsonify({'skillsets': skillsets})

@app.route('/api/skillset/<int:skillset_id>', methods=['GET'])
def get_skillset(skillset_id):
	skillset = [skillset for skillset in skillsets if skillset['skillset_ID'] == skillset_id]
	if len(skillset) == 0:
		abort(404)
	return jsonify({'skillset': skillset[0]})
'''

# API
@app.route('/api/job', methods=['GET'])
def get_jobs():
	jobs = Job.query.all()
	return jsonify(jobs)

@app.route('/api/job/<int:job_id>', methods=['GET'])
def get_job(job_id):
	job = Job.query.get(job_id)
	if len(job) == 0:
		abort(404)
	return jsonify(job)

@app.route('/api/company', methods=['GET'])
def get_companies():
	companies = Company.query.all()
	return jsonify([comEle.serialize() for comEle in companies])
		
@app.route('/api/company/<int:company_id>', methods=['GET'])
def get_company(company_id):
	company = Company.query.get(company_id)
	Result = jsonify([company.serialize()])
	if len(company) == 0:
		abort(404)
	return Result

@app.route('/api/location', methods=['GET'])
def get_locations():
	locations = Location.query.all()
	return jsonify([locEle.serialize() for locEle in locations])

@app.route('/api/location/<int:location_id>', methods=['GET'])
def get_location(location_id):
	location = Location.query.get(location_id)
	Result = jsonify(location.serialize())
	if len(Result) == 0:
		abort(404)
	return Result
	
#Member
@app.route('/api/member', methods=['GET'])
def get_team_member():
	return jsonify(member)

@app.route('/api/language', methods=['GET'])
def get_languages():
	languages = Language.query.all()
	return jsonify([langEle.serialize() for langEle in languages])

@app.route('/api/language/<int:language_id>', methods=['GET'])
def get_language(language_id):
	language = Language.query.get(language_id)
	#print(type(language))
	langResult = jsonify([language.serialize()])
	#print(type(langResult))
	if len(langResult) == 0:
		abort(404)
	return langResult

@app.route('/api/skillset', methods=['GET'])
def get_skillsets():
	skillsets = Skillset.query.all()
	return jsonify(skillsets)

@app.route('/api/skillset/<int:skillset_id>', methods=['GET'])
def get_skillset(skillset_id):
	skillset = Skillset.query.get(skillset_id)
	if len(skillset) == 0:
		abort(404)
	return jsonify(skillset)






#Dynamic pages
@app.route('/language')
def get_languages_page():
	return render_template('languages.html', langJson=languages)

@app.route('/language/<name>')
def get_language_page(name=None):
	name = name.replace(" ", "");
	#need name redirection
	if(name == "C#") :
		name = "Csharp"
	elif(name == "VisualBasic") :
		name = "Visual Basic"
	elif(name == "VisualBasic.NET") :
		name = "Visual Basic.NET"
	# language = Language.query.filterBy('language_name' == name)
	language = [language for language in languages if language['language_name'] == name]
	language=language[0]
	return render_template('language.html', langJson=language, langsJson=languages, cmpyJson=companies, jobJson=jobs, locJson=locations, skillsetJson=skillsets)

@app.route('/location')
def get_locations_page():
	return render_template('locations.html', langJson=languages, cmpyJson=companies, locJson=locations)

@app.route('/location/<name>')
def get_location_page(name=None):
	location = [location for location in locations if location['location_name'] == name]
	location = location[0]
	return render_template('location.html', locJson = location, langJson=languages, cmpyJson=companies, locsJson=locations, jobJson=jobs, skillsetJson=skillsets)

@app.route('/skillset/<name>')
def get_skillset_page(name=None):
	skillset = [skillset for skillset in skillsets if skillset['skillset_name'] == name]
	skillset = skillset[0]
	return render_template('skillset.html', skillsetJson=skillset, jobJson=jobs, locJson=locations, cmpyJson=companies, langJson=languages)

@app.route('/job/<name>')
def get_job_page(name=None):
	job = [job for job in jobs if job['job_title'] == name]
	job = job[0]
	return render_template('job.html', jobsJson=jobs,  jobJson=job, cmpyJson=companies, langJson=languages, locJson=locations, skillsetJson=skillsets)

@app.route('/company')
def get_companies_page():
	return render_template('companies.html',langJson=languages, cmpyJson=companies, locJson=locations)

@app.route('/company/<name>')
def get_company_page(name=None):
	company = [company for company in companies if company['company_name'] == name]
	company = company[0]
	return render_template('company.html', cmpyJson = company, langJson=languages, cmpysJson=companies, locsJson=locations, jobJson=jobs, skillsetJson=skillsets)

@app.route('/about')
def get_about_page():
	return render_template('about.html', memJson=members)

@app.route('/modeldoc')
def get_model_doc_page():
	return send_from_directory('.', 'models.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')
