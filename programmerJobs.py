import os
import subprocess
from flask import Flask, jsonify, abort, render_template, redirect, send_from_directory, request
from flask.ext.sqlalchemy import SQLAlchemy
# import flask.ext.whooshalchemy as whooshalchemy
import json

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['WHOOSH_BASE'] = "$VIRTUAL_ENV/lib/python2.7/site-packages"
db = SQLAlchemy(app)

from models import *

# whooshalchemy.whoosh_index(app, Job)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))


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


# The following are examples of different templates in action
@app.route('/')
def root():
    return redirect('http://104.130.229.90:5000/index', code=302)


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


@app.route('/search', methods=['GET', 'POST'])
def search():
    query_string = request.query_string
    query_split = query_string.split("=")
    return render_template('searching.html', queryField=query_split[1])


@app.route('/search/<query>')
def get_search(query=None):
    # job_search_results = Job.query.whoosh_search(query, limit=10)
    # return render_template('search_results.html', job_search_results=job_search_results)
    queryList = query.split("+")
    whooshResult = Job.query.whoosh_search('software').all()
    print(whooshResult)
    print(len(whooshResult))

    #query in our way. (brute force!)
    # we need to support both 'and' and 'or' search 
    # and since whoosh isn't doing it's job, we need to write our own
    # First, we iterate through query keyword and find all qualified models(language, company, skillset, location) and store it
    # then, iterate through all the job, check if each job matches queried model that we picked on previous step
    # so basically, iterate through jobs and see if all attribute(lang, cmpy, skill, loc) mateches query.
    # if so, add on 'and match' list. 
    # else if job had match at least one attrib, add on 'or match' list
    # end of job iteration
    # on search result page, display two dataTable, one for 'and' search and one for 'or' search.
    # endofsearch.


    #Whoosh is much more clean and beautiful btw...hehe...

    #iterating through 
    queryFieldList = []
    queryLanguageList = []
    queryCompanyList = []
    querySkillsetList = []
    queryLocationList = []
    for queryWord in queryList:
	queryWord = queryWord.title()
	print("querying: " + queryWord)
	queriedLang = db.session.query(Language).filter(Language.language_name == queryWord).first()
	if queriedLang is not None:
	    queryLanguageList.append(queriedLang)
	#queryLanguageList.append(db.session.query(Language).filter(Language.language_name == queryWord).first())
	queriedCmpy = db.session.query(Company).filter(Company.company_name == queryWord).first()
	if queriedCmpy is not None:
	    queryCompanyList.append(queriedCmpy)
	#queryCompanyList.append(db.session.query(Company).filter(Company.company_name == queryWord).first())
	queriedSkill = db.session.query(Skillset).filter(Skillset.skillset_name == queryWord).first()
	if queriedSkill is not None:
	    querySkillsetList.append(queriedSkill)
	#querySkillsetList.append(db.session.query(Skillset).filter(Skillset.skillset_name == queryWord).first())
	queriedLoc = db.session.query(Location).filter(Location.location_name == queryWord).first()
	if queriedLoc is not None:
	    queryLocationList.append(queriedLoc)
	#queryLocationList.append(db.session.query(Location).filter(Location.location_name == queryWord).first())

    jobs = Job.query.all()
    queriedJobList = []   
    matchLang = False
    matchCmpy = False
    matchSkill = False
    matchLoc = False

    andMatchList = []
    orMatchList = []

    print(queryLanguageList)
    print(queryCompanyList)
    print(querySkillsetList)
    print(queryLocationList)
 
    for singleJob in jobs :
	matchLang = False
	matchCmpy = False
	matchSkill = False
	matchLoc = False
	for qLang in queryLanguageList :
	    if qLang is not None :
		if singleJob.languages[0].language_id == qLang.language_id:
			matchLang = True
	for qCmpy in queryCompanyList :
	    if qCmpy is not None:
		if singleJob.company_id == qCmpy.company_id :
			matchCmpy = True
	for qSkill in querySkillsetList :
	    if qSkill is not None:
		if singleJob.skillsets[0].skillset_id == qSkill.skillset_id:
			matchSkill = True
	for qLoc in queryLocationList :
	    if qLoc is not None:
		if singleJob.location_id == qLoc.location_id :
			matchLoc = True

	if(matchLang or matchCmpy or matchSkill or matchLoc):
		orMatchList.append(singleJob)

	#for and match, some model list can be empty, which we need to set true to do 'and' search
	if(len(queryLanguageList) == 0):
		matchLang = True
	if(len(queryCompanyList) == 0):
		matchCmpy = True
	if(len(querySkillsetList) == 0):
		matchSkill = True
	if(len(queryLocationList) == 0):
		matchLoc = True

	if(matchLang and matchCmpy and matchSkill and matchLoc):
		andMatchList.append(singleJob)

	languages = Language.query.all()
	locations = Location.query.all()
	companies = Company.query.all()
	skillsets = Skillset.query.all()
    return render_template('search_results.html', queryList=queryList, orMatchList=orMatchList, andMatchList=andMatchList, langJson=languages, locJson=locations, cmpyJson=companies, skillsetJson=skillsets)


# API
@app.route('/api/job', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify(Jobs=[job.serialize() for job in jobs])


@app.route('/api/job/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        abort(jsonify({"error": "Item does not exist"}))
    return jsonify(job.serialize())


@app.route('/api/company', methods=['GET'])
def get_companies():
    companies = Company.query.all()
    return jsonify(Companies=[comEle.serialize() for comEle in companies])


@app.route('/api/company/<int:company_id>', methods=['GET'])
def get_company(company_id):
    company = Company.query.get(company_id)
    if not company:
        abort(jsonify({"error": "Item does not exist"}))
    return jsonify(company.serialize())


@app.route('/api/location', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify(locations=[locEle.serialize() for locEle in locations])


@app.route('/api/location/<int:location_id>', methods=['GET'])
def get_location(location_id):
    location = Location.query.get(location_id)
    if not location:
        abort(jsonify({"error": "Item does not exist"}))
    return jsonify(location.serialize())


@app.route('/api/member', methods=['GET'])
def get_team_member():
    member = Member.query.all()
    return jsonify(Members=[memEle.serialize() for memEle in member])


@app.route('/api/language', methods=['GET'])
def get_languages():
    languages = Language.query.all()
    return jsonify(languages=[langEle.serialize() for langEle in languages])


@app.route('/api/language/<int:language_id>', methods=['GET'])
def get_language(language_id):
    language = Language.query.get(language_id)
    if not language:
        abort(jsonify({"error": "Item does not exist"}))
    return jsonify(language.serialize())


@app.route('/api/skillset', methods=['GET'])
def get_skillsets():
    skillsets = Skillset.query.all()
    return jsonify(Skillsets=[skillset.serialize() for skillset in skillsets])


@app.route('/api/skillset/<int:skillset_id>', methods=['GET'])
def get_skillset(skillset_id):
    skillset = Skillset.query.get(skillset_id)
    if not skillset:
        abort(jsonify({"error": "Item does not exist"}))
    return jsonify(skillset.serialize())


# use of others api
@app.route('/api/freespirit', methods=['POST'])
def get_freespirit():
    drinks = json.load(open('drinks.json', 'r'))
    ingredients = json.load(open('ingredients.json', 'r'))
    lst = request.form.getlist("lst")

    get_ingre = {}
    results = []
    for selection in lst:
        for drink_dic in drinks:
            if selection == drink_dic['name']:
                get_ingre = drink_dic['ingredients']
                for select in get_ingre.keys():
                    for ingredient_dic in ingredients:
                        if select == ingredient_dic['id']:
                            results.append(ingredient_dic['name'])

    '''
    print ""
    find_drink = True
    res_drink = []

    for drink_dic in drinks:
        find_drink = True
        for i in lst_ing:
            if i not in drink_dic['ingredients'].keys():
                find_drink = False
        if find_drink:
            res_drink.append(drink_dic['name'])

    for rd in res_drink:
        print rd
    '''
    return render_template('drinks.html', ingredients_result=results)


@app.route('/api/freespirit', methods=['GET'])
def get_drinks():
    drinks = json.load(open('drinks.json', 'r'))
    ret = []
    for drink_dic in drinks:
        ret.append(drink_dic['name'])

    return render_template('drinks.html', drinks_lst=ret)


# Dynamic pages
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

    return render_template('language.html', langJson=language, langsJson=languages, cmpyJson=companies, jobJson=jobs,
                           locJson=locations, skillsetJson=skillsets)


@app.route('/location')
def get_locations_page():
    locations = Location.query.all()
    companies = Company.query.all()
    languages = Language.query.all()
    return render_template('locations.html', langJson=languages, cmpyJson=companies, locJson=locations)


@app.route('/location/<int:id>')
def get_location_page(id=None):
    # location = [location for location in locations if location['location_name'] == name]
    # location = location[0]
    location = Location.query.get(id)
    languages = Language.query.all()
    jobs = Job.query.all()
    companies = Company.query.all()
    locations = Location.query.all()
    skillsets = Skillset.query.all()
    return render_template('location.html', locJson=location, langJson=languages, cmpyJson=companies,
                           locsJson=locations, jobJson=jobs, skillsetJson=skillsets)

@app.route('/skillset')
def get_skillsets_page():
    locations = Location.query.all()
    companies = Company.query.all()
    languages = Language.query.all()
    skillsets = Skillset.query.all()
    return render_template('skillsets.html', langJson=languages, cmpyJson=companies, locJson=locations, skillsetJson=skillsets)

@app.route('/skillset/<int:id>')
def get_skillset_page(id=None):
    skillset = Skillset.query.get(id)
    languages = Language.query.all()
    jobs = Job.query.all()
    companies = Company.query.all()
    locations = Location.query.all()
    skillsets = Skillset.query.all()
    # skillset = [skillset for skillset in skillsets if skillset['skillset_name'] == name]
    # skillset = skillset[0]
    return render_template('skillset.html', skillsetJson=skillset, jobJson=jobs, locJson=locations, cmpyJson=companies,
                           langJson=languages)


@app.route('/job/<int:id>')
def get_job_page(id=None):
    job = Job.query.get(id)
    languages = Language.query.all()
    jobs = Job.query.all()
    companies = Company.query.all()
    locations = Location.query.all()
    skillsets = Skillset.query.all()
    # job = [job for job in jobs if job['job_title'] == name]
    # job = job[0]
    return render_template('job.html', jobsJson=jobs,  jobJson=job, cmpyJson=companies, langJson=languages,
                           locJson=locations, skillsetJson=skillsets)


@app.route('/company')
def get_companies_page():
    companies = Company.query.all()
    companies = Company.query.all()
    locations = Location.query.all()
    return render_template('companies.html', cmpyJson=companies)


@app.route('/company/<int:id>')
def get_company_page(id=None):
    company = Company.query.get(id)
    languages = Language.query.all()
    jobs = Job.query.all()
    companies = Company.query.all()
    locations = Location.query.all()
    skillsets = Skillset.query.all()
    return render_template('company.html', cmpyJson=company, cmpysJson=companies, locJson=locations,
                           langJson=languages, jobJson=jobs, skillsetJson=skillsets)


@app.route('/about')
def get_about_page():
    members = Member.query.all()
    return render_template('about.html', memJson=members)


@app.route('/modeldoc')
def get_model_doc_page():
    return send_from_directory('.', 'models.html')


@app.route('/drink')
def get_drink_page():
    return render_template('drink.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
