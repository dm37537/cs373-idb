import os
import subprocess
from flask import Flask, jsonify, abort, render_template, redirect, send_from_directory, request
from flask.ext.sqlalchemy import SQLAlchemy
# import flask.ext.whooshalchemy as whooshalchemy
import json
import urllib

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
    if query_string is None or query_string is "":
        abort(404)
    query_string = query_string.replace("+", "tempQueryDivider")
    query_string = query_string.replace(",", "")
    query_string = query_string.replace(".", "")
    query_split = query_string.split("=")
    print(query_split)
    return render_template('searching.html', queryField=query_split[1])


@app.route('/search/<query>')
def get_search(query=None):
    if query == None :
        abort(404)
    # job_search_results = Job.query.whoosh_search(query, limit=10)
    # return render_template('search_results.html', job_search_results=job_search_results)
    print(query)
    queryList = query.split("tempQueryDivider")
    queryList = [urllib.unquote(queryItem) for queryItem in queryList]
    print(queryList)
    tempQuery = []
    #make first character capital
    for qEle in queryList :
        tempQuery.append(qEle.title())
    queryList = tempQuery
    #remove duplicated element in list
    queryList = list(set(queryList))
    whooshResult = Job.query.whoosh_search('software').all()
    # print(whooshResult)
    # print(len(whooshResult))

    #filter bad query, separate query for each model
    jobTitleQueryField = []
    langQueryField = []
    cmpyQueryField = []
    skillQueryField = []
    locQueryField = []
    badQueryField = []

    dirtyFlag = False

    for queryWord in queryList:
        dirtyFlag = False
	print("querying = " + queryWord)
        queryWord = queryWord.lower()
	print("query.lower() = " + queryWord)
        queriedJobTitle = Job.query.filter(Job.job_title.ilike("%"+queryWord+"%")).all()
        if len(queriedJobTitle) > 0:
            for jobModel in queriedJobTitle :
                jobTitle = jobModel.job_title.split(" ")
		jobTitle = [item.lower() for item in jobTitle]
                #look for perfect word match
                if queryWord in jobTitle :
                    jobTitleQueryField.append(queryWord)
                    dirtyFlag = True
                    break
        queriedLang = Language.query.filter(Language.language_name.ilike("%"+queryWord+"%")).all()
        if len(queriedLang) > 0:
            for langModel in queriedLang:
                langName = langModel.language_name.split(" ")
		langName = [item.lower() for item in langName]
		print(langName)
                if queryWord in langName :
                    langQueryField.append(queryWord)
                    dirtyFlag = True
                    break
        queriedCmpy = Company.query.filter(Company.company_name.ilike("%"+queryWord+"%")).all()
        if len(queriedCmpy) > 0:
            for cmpyModel in queriedCmpy:
                cmpyName = cmpyModel.company_name.split(" ")
                cmpyName = [item.lower() for item in cmpyName]
		print(cmpyName)
                if queryWord in cmpyName :
                    cmpyQueryField.append(queryWord)
                    dirtyFlag = True
                    break
        queriedSkill = Skillset.query.filter(Skillset.skillset_name.ilike("%"+queryWord+"%")).all()
        if len(queriedSkill) > 0:
            for skillModel in queriedSkill:
                skillsetName = skillModel.skillset_name.split(" ")
		skillsetName = [item.lower().replace(",","") for item in skillsetName]
                print(skillsetName)
		if queryWord in skillsetName:
                    skillQueryField.append(queryWord)
                    dirtyFlag = True
                    break
        queriedLoc = Location.query.filter(Location.location_name.ilike("%"+queryWord+"%")).all()
        if len(queriedLoc) > 0:
            for locModel in queriedLoc:
                locName = locModel.location_name.split(" ")
		locName = [item.lower().replace(",","") for item in locName]
		print("locName = " )
		print(locName)
                if queryWord in locName:
                    locQueryField.append(queryWord)
                    dirtyFlag = True
                    break
        if not dirtyFlag:
            badQueryField.append(queryWord)

    jobs = Job.query.all()
    languages = Language.query.all()
    # print(type(languages))
    locations = Location.query.all()
    companies = Company.query.all()
    skillsets = Skillset.query.all()

    andMatchList = []
    orJobTitleMatchList = []
    orLangMatchList = []
    orCmpyMatchList =[]
    orLocMatchList = []
    orSkillMatchList = []
    globalMatchSet = set()

    for jobDict in jobs :
        jobTitleCounter = 0
        if len(jobTitleQueryField) > 0:
            #if it has element
            for queryWord in jobTitleQueryField :
                if queryWord in jobDict.job_title.lower() :
                    jobTitleCounter += 1

        langCounter = 0
        if len(langQueryField) > 0:
            for queryWord in langQueryField :
                langID = jobDict.languages[0].language_id
                langModel = languages[langID -1]
                if queryWord == langModel.language_name.lower() :
                    langCounter += 1

        cmpyCounter = 0
        if len(cmpyQueryField) > 0:
            for queryWord in cmpyQueryField :
                cmpyId = jobDict.company_id
                cmpyModel = companies[cmpyId - 1]
                if queryWord in cmpyModel.company_name.lower() :
                    cmpyCounter += 1

        skillCounter = 0
        if len(skillQueryField) > 0:
            for queryWord in skillQueryField :
                skillId = jobDict.skillsets[0].skillset_id
                skillModel = skillsets[skillId - 1]
                if queryWord in skillModel.skillset_name.lower() :
                    skillCounter += 1

        locCounter = 0
        if len(locQueryField) > 0:
            for queryWord in locQueryField :
                locId = jobDict.location_id
                locModel = locations[locId - 1]
                if queryWord in locModel.location_name.lower() :
                    locCounter += 1

        # print("jobTitleCounter = " + str(jobTitleCounter))
        # print("langCounter = " + str(langCounter))
        # print("cmpyCounter = " + str(cmpyCounter))
        # print("skillCounter = " + str(skillCounter))
        # print("locCounter = " + str(locCounter))

        if jobTitleCounter is len(jobTitleQueryField) and langCounter is len(langQueryField) and cmpyCounter is len(cmpyQueryField) and skillCounter is len(skillQueryField) and locCounter >= 0 :
            #perfect match
            if len(badQueryField) == 0:
                #if there is badquery, it won't find any perfect match
                andMatchList.append(jobDict)
        #if jobTitleCounter > 0 or langCounter > 0 or cmpyCounter > 0 or skillCounter > 0 or locCounter > 0 :
         #   orMatchList.append(jobDict)
	
	if jobTitleCounter > 0:
	    orJobTitleMatchList.append(jobDict)
	if langCounter > 0:
	    orLangMatchList.append(jobDict)
	if cmpyCounter >0:
	    orCmpyMatchList.append(jobDict)
	if skillCounter > 0:
	    orSkillMatchList.append(jobDict)
	if locCounter > 0:
	    orLocMatchList.append(jobDict)

    #remove duplicates
    for andMatchJob in andMatchList:
	if andMatchJob in orJobTitleMatchList:
	    orJobTitleMatchList.remove(andMatchJob)
   
    for orJobTitleMatchJob in orJobTitleMatchList:
	if orJobTitleMatchJob in orCmpyMatchList:
	    orCmpyMatchList.remove(orJobTitleMatchJob)

    for orCmpyMatchJob in orCmpyMatchList:
	if orCmpyMatchJob in orLocMatchList:
	    orLocMatchList.remove(orCmpyMatchJob)

    for orLocMatchJob in orLocMatchList:
	if orLocMatchJob in orLangMatchList:
	    orLangMatchList.remove(orLocMatchJob)

    for orLangMatchJob in orLangMatchList:
	if orLangMatchJob in orSkillMatchList:
	    orSkillMatchList.remove(orLangMatchJob)

    # print("andMatch = ")
    # print(andMatchList)
    # print("orMatch = ")
    # print(orMatchList)

    # matchJobTitle = False
    # matchLang = False
    # matchCmpy = False
    # matchSkill = False
    # matchLoc = False

    # print(queryLanguageList)
    # print(queryCompanyList)
    # print(querySkillsetList)
    # print(queryLocationList)

    jobTitleListLen = len(jobTitleQueryField)
    langListLen = len(langQueryField)
    cmpyListLen = len(cmpyQueryField)
    skillListLen = len(skillQueryField)
    locListLen = len(locQueryField)
 
    # totalLen = langListLen + cmpyListLen + skillListLen + locListLen + jobTitleListLen
    boldList = [langListLen, cmpyListLen, skillListLen, locListLen, jobTitleListLen]
    # print(boldList)

    languages = Language.query.all()
    locations = Location.query.all()
    companies = Company.query.all()
    skillsets = Skillset.query.all()
    
    # if totalLen is 1:
    #     orMatchList =[]
    
    return render_template('search_results.html', queryList=queryList, orJobTitleMatchList=orJobTitleMatchList, orLangMatchList=orLangMatchList, orCmpyMatchList=orCmpyMatchList, orSkillMatchList=orSkillMatchList, orLocMatchList=orLocMatchList, andMatchList=andMatchList, boldList=boldList, langJson=languages, locJson=locations, cmpyJson=companies, skillsetJson=skillsets)


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
    if not languages:
        abort(404)
    return render_template('languages.html', langJson=languages)


@app.route('/language/<int:id>')
def get_language_page(id=None):
    language = Language.query.get(id)
    languages = Language.query.all()
    if not language:
        abort(404)
    jobs = Job.query.all()
    companies = Company.query.all()
    locations = Location.query.all()
    skillsets = Skillset.query.all()

    return render_template('language.html', langJson=language, langsJson=languages, cmpyJson=companies, jobJson=jobs,
                           locJson=locations, skillsetJson=skillsets)


@app.route('/location')
def get_locations_page():
    locations = Location.query.all()
    if not locations:
        abort(404)
    companies = Company.query.all()
    languages = Language.query.all()
    return render_template('locations.html', langJson=languages, cmpyJson=companies, locJson=locations)


@app.route('/location/<int:id>')
def get_location_page(id=None):
    # location = [location for location in locations if location['location_name'] == name]
    # location = location[0]
    location = Location.query.get(id)
    if not location:
        abort(404)
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
    if not skillset:
        abort(404)
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
    if not job:
        abort(404)
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
    if not companies:
        abort(404)
    locations = Location.query.all()
    return render_template('companies.html', cmpyJson=companies)


@app.route('/company/<int:id>')
def get_company_page(id=None):
    company = Company.query.get(id)
    if not company:
        abort(404)
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
    if not members:
        abort(404)
    return render_template('about.html', memJson=members)


@app.route('/modeldoc')
def get_model_doc_page():
    return send_from_directory('.', 'models.html')


@app.route('/drink')
def get_drink_page():
    return render_template('drink.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
