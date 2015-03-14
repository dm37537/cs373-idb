import os
from flask import Flask, jsonify
import json

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])

#DATABASE = os.path.join(app.root_path, 'flaskr.db')
app.config.update(dict(
	DEBUG = True,
	SECRET_KEY = 'development key',
	USERNAME = 'admin',
	PASSWORD = 'default'
))
app.config.from_envvar('PROJECT_SETTINGS', silent=True)

"""
def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])

def init_db():
	db = get_db()
	with app.open_resource('schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()

def initdb_command():
	init_db()
	print('Initialized the database.')

def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):	
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()
"""
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

# API FUNCTIONALITY
@app.route('/job', methods=['GET'])
def get_tasks():
	return jsonify({'jobs': jobs})

@app.route('/job/<int:job_id>', methods=['GET'])
def get_job(job_id):
	job = [job for job in jobs if job['id'] == job_id]
	if len(task) == 0:
		abort(404)
	return jsonify({'job': job[0]})

@app.route('/company', methods=['GET'])
def get_companies():
    return jsonify({'companies': companies})
	    
@app.route('/company/<int:company_id>', methods=['GET'])
def company_job(company_id):
	company = [company for company in companies if company['id'] == company_id]
	if len(task) == 0:
		abort(404)
	return jsonify({'company': company[0]})

if __name__ == '__main__':
	app.run()
