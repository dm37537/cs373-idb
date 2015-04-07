import os
from flask import Flask, jsonify, abort, render_template, redirect, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
import json
from models import db, Job, Company, Language, Skillset, Location
#import tests

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
#db = SQLAlchemy(app)
db.init_app(app)

app.config.update(dict(
	SECRET_KEY = 'development key',
	USERNAME = 'admin',
	PASSWORD = 'default'
))
#app.config.from_envvar('PROJECT_SETTINGS', silent=True)

def init_db():
	db.drop_all()
	db.create_all()
	#with app.open_resource('schema.sql', mode='r') as f:
	#	db.cursor().executescript(f.read())

def populate_db():
	with app.open_resource('insert.sql', mode='r') as f:
		db.cursor().execute(f.read)

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

f = open('Rank.json')
rank = json.load(f)
f.close()

f = open('Member.json')
member = json.load(f)
f.close()

# The following are examples of different templates in action
@app.route('/')
def root():
	return redirect('http://104.130.229.90:5000/index.html', code=302)
	# return redirect('http://127.0.0.1:5000/index.html', code=302)

@app.route('/index.html')
def index():
	return send_from_directory('.', 'index.html')

@app.route('/test')
def test():
	return send_from_directory('.', 'runTest.php')

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


#Rank
@app.route('/api/rank', methods=['GET'])
def get_language_rank():
	return jsonify({'rank': rank})
	
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
	return jsonify(companies)
		
@app.route('/api/company/<int:company_id>', methods=['GET'])
def get_company(company_id):
	company = Company.query.get(company_id)
	if len(company) == 0:
		abort(404)
	return jsonify(company)

@app.route('/api/location', methods=['GET'])
def get_locations():
	locations = Location.query.all()
	return jsonify(locations)

@app.route('/api/location/<int:location_id>', methods=['GET'])
def get_location(location_id):
	location = Location.query.get(location_id)
	if len(location) == 0:
		abort(404)
	return jsonify(location)

#Rank
@app.route('/api/rank', methods=['GET'])
def get_language_rank():
	return jsonify(rank)
	
#Member
@app.route('/api/member', methods=['GET'])
def get_team_member():
	return jsonify(member)

@app.route('/api/language', methods=['GET'])
def get_languages():
	languages = Language.query.all()
	return jsonify(languages)

@app.route('/api/language/<int:language_id>', methods=['GET'])
def get_language(language_id):
	language = Language.query.get(language_id)
	if len(language) == 0:
		abort(404)
	return jsonify(language)

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
def get_language_home_page():
	return render_template('language_home.html')

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

	language = [language for language in languages if language['language_name'] == name]
	language=language[0]
	return render_template('language.html', langName=language['language_name'], langId=language['language_ID'])

if __name__ == '__main__':
	app.run(host='0.0.0.0')
