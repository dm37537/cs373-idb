import os
from flask import Flask, jsonify

app = Flask(__name__)

app.config.update(dict(
	DATABASE = os.path.join(app.root_path, 'flaskr.db'),
	DEBUG = True,
	SECRET_KEY = 'development key',
	USERNAME = 'admin',
	PASSWORD = 'default'
))
app.config.from_envvar('PROJECT_SETTINGS', silent=True)

def connect_db():
	""" Connects to the database """
	rv = sqlite3.connect(app.config['DATABASE'])

def init_db():
	db = get_db()
	with app.open_resource('schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()

@app.cli.command('initdb')
def initdb_command():
	""" Creates the database tables """
	init_db()
	print('Initialized the database.')

def get_db():
	""" Opens a new database connection if there is none yet for the
		current application context.
	"""
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db(error):	
	""" Closes the database again at the end of the request"""
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()

# Data structures to store info to be replaced with database
jobs = [
	{
		'This'
	},
	{
		'Works'
	}
]

companies = [
	{
		'This'
	},
	{
		'Works'
	}
]

# The following are examples of different templates in action

@app.route('/')
def index():
	return 'Hello, World'

# API FUNCTIONALITY
@app.route('/job', methods=['GET'])
def get_tasks():
	return jsonify({'Jobs': jobs})

@app.route('/job/<int:job_id>', methods=['GET'])
def get_job(job_id):
	job = [job for job in jobs if job['id'] == job_id]
	if len(task) == 0:
		abort(404)
	return jsonify({'job': job[0]})

@app.route('/company', methods=['GET'])
def get_tasks():
    return jsonify({'Companies': companies})
	    
@app.route('/company/<int:company_id>', methods=['GET'])
def company_job(company_id):
	company = [company for company in companies if company['id'] == company_id]
	if len(task) == 0:
		abort(404)
	return jsonify({'company': company[0]})


if __name__ == '__main__':
	app.run()
