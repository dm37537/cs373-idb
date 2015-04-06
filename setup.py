from setuptools import setup

setup(
	name='Programmer Jobs',
	version='1.0',
	long_description='',
	install_requires=[
	'Flask',
	'Flask-SQLAlchemy'
	],
	dependency_links=['http://www.postgresql.org/ftp/source/v9.4.1/postgresql-9.4.1.tar.gz']
)
