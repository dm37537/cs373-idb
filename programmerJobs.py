import os
from flask import Flask, jsonify, abort
import json

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])

app.config.update(dict(
	DEBUG = True,
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
def index():
	return 'Hello, World'

# API
@app.route('/job', methods=['GET'])
def get_jobs():
	return jsonify({'jobs': jobs})

@app.route('/job/<int:job_id>', methods=['GET'])
def get_job(job_id):
	job = [job for job in jobs if job['id'] == job_id]
	if len(job) == 0:
		abort(404)
	return jsonify({'job': job[0]})

@app.route('/company', methods=['GET'])
def get_companies():
    return jsonify({'companies': companies})
	    
@app.route('/company/<int:company_id>', methods=['GET'])
def get_company(company_id):
	company = [company for company in companies if company['Company_ID'] == company_id]
	if len(company) == 0:
		abort(404)
	return jsonify({'company': company[0]})

@app.route('/location', methods=['GET'])
def get_locations():
    return jsonify({'locations': locations})

@app.route('/location/<int:location_id>', methods=['GET'])
def get_location(location_id):
	location = [location for location in locations if location['Location_ID'] == location_id]
	if len(location) == 0:
		abort(404)
	return jsonify({'location': location[0]})

@app.route('/language', methods=['GET'])
def get_languages():
    return jsonify({'languages': languages})

@app.route('/language/<int:language_id>', methods=['GET'])
def get_language(language_id):
	language = [language for language in languages if language['Language_ID'] == language_id]
	if len(language) == 0:
		abort(404)
	return jsonify({'language': language[0]})

@app.route('/skillset', methods=['GET'])
def get_skillsets():
    return jsonify({'skillsets': skillsets})

@app.route('/skillset/<int:skillset_id>', methods=['GET'])
def get_skillset(skillset_id):
	skillset = [skillset for skillset in skillsets if skillset['Skillset_ID'] == skillset_id]
	if len(skillset) == 0:
		abort(404)
	return jsonify({'skillset': skillset[0]})

if __name__ == '__main__':
	app.run()
