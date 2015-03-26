import os
from flask import Flask, jsonify, abort, render_template, redirect, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
import json
#import tests

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

app.config.update(dict(
	SECRET_KEY = 'development key',
	USERNAME = 'admin',
	PASSWORD = 'default'
))
app.config.from_envvar('PROJECT_SETTINGS', silent=True)

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

# The following are examples of different templates in action
@app.route('/')
def root():
	return redirect('http://104.130.229.90:5000/index.html', code=302)

@app.route('/index.html')
def index():
	return send_from_directory('.', 'index.html')

@app.route('/test')
def test():
	return send_from_directory('.', 'runTest.html')

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

if __name__ == '__main__':
	app.run(host='0.0.0.0')
