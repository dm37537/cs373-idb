import os

app = Flask(__name__)

app.config.update(dict(
	DATABASE = os.path.join(app.root_path, 'flaskr.db'),
	DEBUG = True,
	SECRET_KEY = 'development key',
	USERNAME = 'admin'
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

# The following are examples of different templates in action

@app.route('/')
def show_entries():
	return None

if __name__ == '__main__':
	app.run()
