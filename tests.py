import unittest
import socket
default_timeout = 10
socket.setdefaulttimeout(default_timeout)

from programmerJobs import *
from models import Job, Company, Location, Language, Skillset
import requests


class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///databaseTest'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # def testAddCompany(self):
    # 	content = (999,'a','as','asd','asdf')
    # 	db.add(content)
    # 	ad.commit(content)

    # def test_create_job(self):
    #     company = Company(company_id=1, name='Google', description='None', site='www.google.com', image='')
    #     db.add(company)
    #     db.commit()
    #     query = Company.query.get(1)
    #     self.assertEqual(company, query)


class ProgrammerJobsTestCase(unittest.TestCase):
    def testCreatingJob(self):
        job = Job(1, 'Software Developer', 1, 1, 'Clickity-Clackity', 'www.google.com')
        assert job.job_title == 'Software Developer'
        assert job.location_id == 1
        assert job.company_id == 1
        assert job.job_description == 'Clickity-Clackity'
        assert job.link == 'www.google.com'

    def testModifyingJob(self):
        job = Job(1, 'Software Developer', 1, 1, 'Clickity-Clackity', 'www.google.com')
        job.job_title = 'Security Engineer'
        job.location_id = 0
        job.company_id = 0
        job.job_description = 'leet h4xxor'
        job.link = 'www.vir.us'
        assert job.job_title == 'Security Engineer'
        assert job.location_id == 0
        assert job.company_id == 0
        assert job.job_description == 'leet h4xxor'
        assert job.link == 'www.vir.us'

    def testModifyingJob2(self):
        job = Job(1, 'Software Developer', 1, 1, 'Clickity-Clackity', 'www.google.com')
        job.job_title = 'CEO'
        job.location_id = 0
        job.company_id = 0
        job.job_description = 'Top dog'
        job.link = 'www.google.com'
        assert job.job_title == 'CEO'
        assert job.location_id == 0
        assert job.company_id == 0
        assert job.job_description == 'Top dog'
        assert job.link == 'www.google.com'

    def testCreatingCompany(self):
        company = Company(1, 'elgooG', 'enigne hcraeS', 'gpj.elgooG', 'www.elgoog.com')
        assert company.company_name == 'elgooG'
        assert company.company_description == 'enigne hcraeS'
        assert company.company_image == 'gpj.elgooG'
        assert company.company_site == 'www.elgoog.com'

    def testModifyingCompany(self):
        company = Company(1, 'elgooG', 'enigne hcraeS', 'gpj.elgooG', 'www.elgoog.com')
        company.company_name = 'bing'
        company.company_description = 'not google'
        company.company_image = 'bell.png'
        company.company_site = 'www.bing.com'
        assert company.company_name == 'bing'
        assert company.company_description == 'not google'
        assert company.company_image == 'bell.png'
        assert company.company_site == 'www.bing.com'

    def testModifyingCompany2(self):
        company = Company(1, 'elgooG', 'enigne hcraeS', 'gpj.elgooG', 'www.elgoog.com')
        company.company_name = 'facebook'
        company.company_description = 'social network'
        company.company_image = 'blue.png'
        company.company_site = 'www.facebook.com'
        assert company.company_name == 'facebook'
        assert company.company_description == 'social network'
        assert company.company_image == 'blue.png'
        assert company.company_site == 'www.facebook.com'

    def testCreatingLocation(self):
        location = Location(1, 'Austin, TX', 'Live music capital of the world', 'austin.jpg')
        assert location.location_name == 'Austin, TX'
        assert location.location_description == 'Live music capital of the world'
        assert location.location_image == 'austin.jpg'

    def testModifyingLocation(self):
        location = Location(1, 'Austin', 'Live music capital of the world', 'austin.jpg')
        location.location_name = 'New York, New York'
        location.location_description = 'City that never sleeps'
        location.location_image = 'newyork.jpg'
        assert location.location_name == 'New York, New York'
        assert location.location_description == 'City that never sleeps'
        assert location.location_image == 'newyork.jpg'

    def testModifyingLocation2(self):
        location = Location(1, 'Austin, TX', 'Live music capital of the world', 'austin.jpg')
        location.location_name = 'San Francisco, CA'
        location.location_description = 'I\'ve been there'
        location.location_image = 'goldengatebridge.jpg'
        assert location.location_name == 'San Francisco, CA'
        assert location.location_description == 'I\'ve been there'
        assert location.location_image == 'goldengatebridge.jpg'

    def testCreatingLanguage(self):
        language = Language(1, 'Spanish', 'taco, burrito, ...', 'sombrero.png', 'large_sombrero.png', 'image.jpg')
        assert language.language_name == 'Spanish'
        assert language.language_image == 'taco, burrito, ...'
        assert language.language_wiki_description == 'sombrero.png'
        assert language.language_description == 'large_sombrero.png'

    def testModifyingLanguage(self):
        language = Language(1, 'Spanish', 'taco, burrito, ...', 'sombrero.png', 'large_sombrero.png', 'image.jpg')
        language.language_name = 'French'
        language.language_description = 'Croissant'
        language.language_image_small = 'crepe.jpg'
        language.language_image_large = 'large_crepe.jpg'
        assert language.language_name == 'French'
        assert language.language_description == 'Croissant'
        assert language.language_image_small == 'crepe.jpg'
        assert language.language_image_large == 'large_crepe.jpg'

    def testModifyingLanguage2(self):
        language = Language(1, 'Spanish', 'taco, burrito, ...', 'sombrero.png', 'large_sombrero.png', 'image.jpg')
        language.language_name = 'English'
        language.language_description = 'Spoken in the USA'
        language.language_image_small = 'merica.jpg'
        language.language_image_large = 'large_merica.jpg'
        assert language.language_name == 'English'
        assert language.language_description == 'Spoken in the USA'
        assert language.language_image_small == 'merica.jpg'
        assert language.language_image_large == 'large_merica.jpg'

    def testCreatingSkillset(self):
        skillset = Skillset(1, 'Mobile Computing', 'walking computers', 'image.jpg', 'wiki description', 'wiki.html')
        assert skillset.skillset_name == 'Mobile Computing'
        assert skillset.skillset_description == 'walking computers'

    def testModifyingSkillset(self):
        skillset = Skillset(1, 'Mobile Computing', 'walking computers', 'image.jpg', 'wiki description', 'wiki.html')
        skillset.skillset_name = 'Android'
        skillset.skillset_description = 'Lollipop'
        assert skillset.skillset_name == 'Android'
        assert skillset.skillset_description == 'Lollipop'

    def testModifyingSkillset2(self):
        skillset = Skillset(1, 'Mobile Computing', 'walking computers', 'image.jpg', 'wiki description', 'wiki.html')
        skillset.skillset_name = 'IOS'
        skillset.skillset_description = 'ipad'
        assert skillset.skillset_name == 'IOS'
        assert skillset.skillset_description == 'ipad'

    def test_getting_nonexisting_job(self):
        req = requests.get('http://104.130.229.90:5000/job/12345678')
        self.assertEqual(req.status_code, 404)
        req.close()

    def test_getting_nonexisting_company(self):
        req = requests.get('http://104.130.229.90:5000/company/12345678')
        self.assertEqual(req.status_code, 404)

    def test_getting_nonexisting_language(self):
        req = requests.get('http://104.130.229.90:5000/language/12345678')
        self.assertEqual(req.status_code, 404)

    def test_getting_nonexisting_location(self):
        req = requests.get('http://104.130.229.90:5000/location/12345678')
        self.assertEqual(req.status_code, 404)

    def test_getting_nonexisting_skillset(self):
        req = requests.get('http://104.130.229.90:5000/skillset/12345678')
        self.assertEqual(req.status_code, 404)


class APITestCase(unittest.TestCase):
    def test_getting_jobs(self):
        expected = {
            "Jobs": [
                {
                    "company_id": 2,
                    "job_description": "Design, configure, and implement our data systems and stream processing "
                                       "pipelines/nCode analytics jobs, web services, and other components/nWork with "
                                       "operations to build and configure maintainable, resource-efficient systems/n"
                                       "Work with data pipelines using Kafka, Cassandra, Spark/nLeverage Event "
                                       "processing technologies to deliver real time analytics features/nDevelop a "
                                       "cloud service that would be processing billions of events a day/nLeverage fast "
                                       "data pipelines for real time analytics on various Oracle SaaS applications/n"
                                       "Contribute ideas for continually improving the team s productivity, job "
                                       "enjoyment, and code quality./nActively mentor junior developers to develop "
                                       "their technical expertise/nHave fun engineering software and scalable systems",
                    "job_id": 1,
                    "job_title": "Software Developer 4",
                    "link": "https://oracle.taleo.net/careersection/2/jobdetail.ftl?job=90953",
                    "location_id": 3
                },
                {
                    "company_id": 2,
                    "job_description": "Are you interested in building Identity infrastructure for the cloud? Oracle s "
                                       "Cloud Infrastructure team is building new Infrastructure-as-a-Service "
                                       "technologies that operate at high scale in a broadly distributed multi-tenant "
                                       "cloud environment. Our customers run their businesses on our cloud, and our "
                                       "mission is to provide them with best in class compute, storage, networking, "
                                       "database, security, and an ever expanding set of foundational cloud-based "
                                       "services./n/nWe re looking for Software Developer with expertise and passion in"
                                       " solving difficult problems in distributed systems, virtualized infrastructure,"
                                       " and highly available services. If this is you, at Oracle you can design and "
                                       "build innovative new systems from the ground up. These are exciting times in "
                                       "our space - we are growing fast, still at an early stage, functioning like a "
                                       "startup and working on ambitious new initiatives. An engineer at any level can "
                                       "have significant technical and business impact./n/nAs a Software Developer, "
                                       "you will own and lead software architecture and development for Authentication "
                                       "and Authorization components of Oracle s Cloud Identity Infrastructure.  You "
                                       "should be a distributed systems generalist, able to build broad systems "
                                       "interactions, while being very hands-on, able to dive deep into any part of the"
                                       " stack and lower level system interactions. You should value simplicity and "
                                       "scale, work comfortably in a collaborative, agile environment, and be excited "
                                       "to learn.",
                    "job_id": 2,
                    "job_title": "Software Developer 2",
                    "link": "https://oracle.taleo.net/careersection/2/jobdetail.ftl?job=86141",
                    "location_id": 3
                },
                {
                    "company_id": 2,
                    "job_description": "Design, develop, troubleshoot and debug software programs for databases, "
                                       "applications, tools, networks etc./n/nAs a member of the software engineering "
                                       "division, you will take an active role in the definition and evolution of "
                                       "standard practices and procedures. Define specifications for significant new "
                                       "projects and specify, design and develop software according to those "
                                       "specifications. You will perform professional software development tasks "
                                       "associated with the developing, designing and debugging of software "
                                       "applications or operating systems./n/nProvide leadership and expertise in the "
                                       "development of new products/services/processes, frequently operating at the "
                                       "leading edge of technology. Recommends and justifies major changes to existing "
                                       "products/services/processes. BS or MS degree or equivalent experience relevant "
                                       "to functional area. 8 more years of software engineering or related "
                                       "experience.",
                    "job_id": 3,
                    "job_title": "Software Developer 5",
                    "link": "https://oracle.taleo.net/careersection/2/jobdetail.ftl?job=60564",
                    "location_id": 2
                },
                {
                    "company_id": 2,
                    "job_description": "Design, develop, troubleshoot and debug software programs for databases, "
                                       "applications, tools, networks etc./n/nAs a member of the software engineering "
                                       "division, you will assist in defining and developing software for tasks "
                                       "associated with the developing, debugging or designing of software applications"
                                       " or operating systems. Provide technical leadership to other software "
                                       "developers. Specify, design and implement modest changes to existing software "
                                       "architecture to meet changing needs./n/nDuties and tasks are varied and complex"
                                       " needing independent judgment. Fully competent in own area of expertise. May "
                                       "have project lead role and or supervise lower level personnel. BS or MS degree"
                                       " or equivalent experience relevant to functional area. 4 years of software "
                                       "engineering or related experience.",
                    "job_id": 4,
                    "job_title": "Software Developer 3",
                    "link": "https://oracle.taleo.net/careersection/2/jobdetail.ftl?job=46894",
                    "location_id": 1
                },
                {
                    "company_id": 1,
                    "job_description": "Build custom front-ends (web and mobile), back-end services, and third-party "
                                       "integrations to automate business processes./nPropose, design, and implement "
                                       "business workflows to streamline asset management lifecycles./nMaintain strong "
                                       "development practices including technical design and writing clean, modular, "
                                       "well tested and self-sustaining code./nCollaborate with business analysts, "
                                       "program managers, end users and other internal teams to translate business "
                                       "requirements into technical solutions that work at Google scale./nIntegrate "
                                       "third-party products with Google s internal systems as well as support and "
                                       "upgrade implemented systems.",
                    "job_id": 5,
                    "job_title": "Application Developer, Corporate Asset Management Engineering",
                    "link": "https://www.google.com/about/careers/search?src=Online/Job+Board/indeed&utm_source=indeed&"
                            "utm_medium=jobaggr&utm_campaign=freeaggr#!t=jo&jid=94815001",
                    "location_id": 5
                },
                {
                    "company_id": 1,
                    "job_description": "Design, write and deliver software to improve the availability, scalability, "
                                       "latency, and efficiency of Google s services./nSolve problems relating to "
                                       "mission critical services and build automation to prevent problem recurrence; "
                                       "with the goal of automating response to all non-exceptional service conditions."
                                       "/nInfluence and create new designs, architectures, standards and methods for "
                                       "large-scale distributed systems./nEngage in service capacity planning and "
                                       "demand forecasting, software performance analysis and system tuning./nConduct "
                                       "periodic on call duties using a follow-the-sun model.",
                    "job_id": 6,
                    "job_title": "Systems Engineer, Site Reliability Engineering",
                    "link": "https://www.google.com/about/careers/search?src=Online/Job+Board/indeed&utm_source=indeed&"
                            "utm_medium=jobaggr&utm_campaign=freeaggr#!t=jo&jid=83835001",
                    "location_id": 4
                },
                {
                    "company_id": 3,
                    "job_description": "* Design, develop, test, troubleshoot, debug, deploy, maintain, document and "
                                       "deliver large-scale, highly distributed, real-time and management systems that "
                                       "are core to effectively managing the supply chain business./n/n* Use Java, "
                                       "object-oriented (OO) design patterns, distributed Oracle databases, and data "
                                       "modeling techniques./n/n* Gather and analyze business and functional "
                                       "requirements, and translate business requirements into technical design "
                                       "specifications./n/n* Serve as a key technical resource in the full development "
                                       "cycle./n/n* Produce comprehensive, usable software documentation./n/n* "
                                       "Recommend changes in development, maintenance and system standards./n/n* Work "
                                       "in an agile development environment, where you are always working on the most "
                                       "important stuff./n/n* Hire, coach, and mentor individuals.",
                    "job_id": 7,
                    "job_title": "Software Development Engineer",
                    "link": "https://en-amazon.icims.com/jobs/219381/software-development-engineer/job?mode=job&iis="
                            "Indeed&iisn=Indeed+%28Free+Posting%29&mobile=false&width=884&height=1200&bga=true&needs"
                            "Redirect=false",
                    "location_id": 2
                },
                {
                    "company_id": 4,
                    "job_description": "Want to create products that more than 1 billion people around the world use? "
                                       "Want to build new features and improve existing products like Photos, Video, "
                                       "Places, NewsFeed, Search, Mobile and Messaging? Want to solve unique, large "
                                       "scale, highly complex technical problems? Facebook is seeking an experienced "
                                       "Software Engineer to join the Products team. You can help build the "
                                       "next-generation systems behind Facebook s products, create web applications "
                                       "that reach millions of people, build high volume servers and be a part of a "
                                       "team that s working to help people connect with each other around the globe. "
                                       "Join us! This position is full-time and is based in our New York office. ",
                    "job_id": 15,
                    "job_title": "Software Engineer, Products",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0IA0000006cPKxMAM",
                    "location_id": 5
                },
                {
                    "company_id": 3,
                    "job_description": "Prime Now is Amazon s newest benefit for Prime members offering one-hour "
                                       "delivery on tens of thousands of items through a new application. Our software "
                                       "accounts for a massive amount of constantly changing variables. We optimize "
                                       "route generation for every item, enabling customers to receive delivery in an "
                                       "hour or less, avoiding a trip to the store. /nWe are looking for a talented Sr."
                                       " Software Engineer to design and build these new systems. The software will "
                                       "need to process thousands of transactions per second across massive data sets. "
                                       "This team handles real-time transportation constraints (weather, traffic and "
                                       "more), optimizes routing algorithms and utilizes machine learning. Are you up "
                                       "to this challenge?/nYou will work on a V1 product and have the autonomy to "
                                       "deliver! ",
                    "job_id": 8,
                    "job_title": "Senior Software Engineer",
                    "link": "https://oracle.taleo.net/careersection/2/jobdetail.ftl?job=86141",
                    "location_id": 1
                },
                {
                    "company_id": 3,
                    "job_description": "Do you want to help developers monetize and advertise their apps across mobile "
                                       "phones and tablets?/n/nWe are looking for a software development engineer to "
                                       "build back-end services for the next generation Mobile Advertising Demand "
                                       "platform. This platform will extend frictionless advertising capabilities for "
                                       "digital and physical goods enabling our customers promote goods through a "
                                       "seamless experience. You will drive innovation on a number of technologies "
                                       "across campaign and image optimization techniques. You will work on a "
                                       "distributed system leveraging AWS that would manage campaigns to meet service "
                                       "level goals. This is a unique opportunity to learn about the advertising "
                                       "supply/demand dynamics and build software solutions to manage delivery of "
                                       "advertising budgets. You will work with partner teams that display ads across "
                                       "all mobile platforms e.g. iOS, Android, HTML5 as well as other advertising "
                                       "exchanges. As a key team member, you will own major deliverables through all "
                                       "aspects of the development cycle: scoping, design, implementation, testing on "
                                       "solutions delivered./n/nYou thrive in a start-up like environment where "
                                       "flexibility, teamwork, and delivering rock solid, customer focused solutions on"
                                       " short timelines is paramount. You enjoy working on complex system software, "
                                       "tackling tough challenges, and feel strongly not only about building good "
                                       "software but about making that software achieve its goals in operational "
                                       "reality. You show a strong sense of ownership, bias for action, agility, "
                                       "creativity, and ingenuity./n/nJoin our team and deliver game changing mobile "
                                       "advertising solutions that engage our customers.",
                    "job_id": 9,
                    "job_title": "Software Development Engineer - Mobile Demand Platform ( ios, Android)",
                    "link": "https://en-amazon.icims.com/jobs/261541/software-development-engineer---mobile-demand-"
                            "platform-%28-ios%2c-android%29/job?mode=job&iis=Indeed&iisn=Indeed+%28Free+Posting%29",
                    "location_id": 2
                },
                {
                    "company_id": 2,
                    "job_description": "Oracle America, Inc. has Applications Developer positions available in Austin, "
                                       "TX. Analyze, design, develop, troubleshoot and debug Oracle Retail Stores "
                                       "Applications. Perform detailed design based on provided high level architecture"
                                       " and design specification.andnbsp; Implement enhancements to the Oracle Retail "
                                       "Stores Applications. Write and execute unit tests.andnbsp; Build SQL queries "
                                       "and assist in system planning, scheduling and implementation. Review "
                                       "integration and regression test plans created by QA and interact with QA and "
                                       "Product Management about problems in the code./nEmployer will accept Master s "
                                       "degree in Computer Science, Computer Engineering, or related technical field. "
                                       "Education or experience must include: 1. Object oriented languages, including "
                                       "Java, Objective C, C/C++; 2. UML and Design Patterns; 3. Designing and "
                                       "implementing new modulesandnbsp; using technologies, including webservices and "
                                       "JEE; 4. Writing SQL queries for Oracle and other databases using SQL and stored"
                                       " procedures; 5. Maintaining and creating new unit tests; 6. Understanding and "
                                       "complying with software development methodologies and processes; 7. "
                                       "Troubleshooting Application Servers deployment issues and security; 8. Mobile "
                                       "application design and development; and, 9. Eclipse and Netbeans or other IDE. "
                                       "Experience may be gained concurrently.",
                    "job_id": 10,
                    "job_title": "Applications Developer 2",
                    "link": "https://oracle.taleo.net/careersection/2/jobdetail.ftl?job=87689",
                    "location_id": 1
                },
                {
                    "company_id": 4,
                    "job_description": "As a software engineer at Oculus Research your job is to figure out what "
                                       "virtual reality looks like 5 years in the future. You ll be part of a multi-"
                                       "disciplinary team pushing on every aspect of the experience: haptics, audio, "
                                       "input, computer vision, optics, display technology, and whatever else we can "
                                       "dream up. Our mission is to keep advancing the VR platform; the work you do "
                                       "here will lay the foundation for VR experiences for years to come. Ideal "
                                       "candidates are exceptional C/C++ programmers who are comfortable working with "
                                       "new technologies at multiple levels in the software stack. We re looking for "
                                       "adaptable coders who are used to owning and writing non-trivial software "
                                       "systems.",
                    "job_id": 11,
                    "job_title": "Software Engineer, Oculus",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0IA000000G46DiMAJ",
                    "location_id": 2
                },
                {
                    "company_id": 4,
                    "job_description": "Partner Engineering is a highly technical team that works with our strategic "
                                       "partners to integrate Facebook and Instagram Platforms into their Web sites, "
                                       "applications, and devices. In this role, you will engage with some of the world"
                                       " s most influential companies and work closely with our world-class engineering"
                                       " and product teams. The ideal candidate will combine excellent technical and "
                                       "business skills to make our partners successful and improve the Facebook and "
                                       "Instagram Platforms. This position is based in our New York office.",
                    "job_id": 12,
                    "job_title": "Partner Engineer, Platform",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0IA000000G3uvoMAB",
                    "location_id": 5
                },
                {
                    "company_id": 4,
                    "job_description": "We re looking for hardcore infrastructure engineers to join the Systems "
                                       "Engineering team. This infrastructure team builds the large, distributed "
                                       "systems that are the heart of Facebook, no easy task. Our code serves millions "
                                       "of requests per second, and it does so with sub-second latency and in a fault "
                                       "tolerant manner. We handle everything from distributed data storage, to "
                                       "synchronization and coordination of large server farms, to building a fast PHP "
                                       "virtual machine for our front end Facebook code. We are looking for candidates "
                                       "who posses a demonstrable, radiant energy towards tackling complexity and "
                                       "building platforms that can scale through multiple orders of magnitude to make "
                                       "the world more open and connected.",
                    "job_id": 13,
                    "job_title": "Software Engineer, Systems",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0IA0000006cQPOMA2",
                    "location_id": 5
                },
                {
                    "company_id": 4,
                    "job_description": "We re looking for data-driven engineers to join the Search and Machine Learning"
                                       " team. As a part of the larger Entities team, which is working to map and "
                                       "connect the high-quality social and entity graph on Facebook, the Search team "
                                       "is focused on building the best location dataset in the world for our location "
                                       "products (mobile Nearby, Graph Search, etc.) and 3rd party developers. The work"
                                       " is a mix of Crowdsourcing (PHP/front-end), Machine Learning (Python/ranking), "
                                       "and Search Features/Ranking (Python/ranking). We are looking for candidates who"
                                       " share a passion for tackling complexity and making sense out of massive "
                                       "datasets using text retrieval, NLP, machine learning and various other "
                                       "optimization techniques.",
                    "job_id": 14,
                    "job_title": "Software Engineer, Search & Machine Learning",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0IA0000006cPbyMAE",
                    "location_id": 5
                },
                {
                    "company_id": 4,
                    "job_description": "Our team is at the intersection of software engineering and digital "
                                       "advertising. This role is for engineers who love to build products and work "
                                       "with partners to realize the full potential of those products. As a Solutions "
                                       "Engineer, you are the engineering lead of your assigned set of partners and are"
                                       " responsible for developing their Facebook technology strategy and executing on"
                                       " it. You will spend 50% of your time working with product engineering teams and"
                                       " writing code. The other 50% you will spend working directly with partners. "
                                       "This is an engineering role with a high bar for problem solving and coding "
                                       "skills. This role is located in our New York, NY office.",
                    "job_id": 16,
                    "job_title": "Solutions Engineer",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0I1200000G4LyeEAF",
                    "location_id": 5
                },
                {
                    "company_id": 4,
                    "job_description": "We are looking for someone that has strong experience developing user "
                                       "interfaces for applications on Android using Android SDK. If you are interested"
                                       " in joining a world-class team of passionate people and industry veterans who "
                                       "like to work hard and play hard, we look forward to hearing from you soon!",
                    "job_id": 17,
                    "job_title": "Software Engineer, Android",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0IA000000CvZ0LMAV",
                    "location_id": 5
                },
                {
                    "company_id": 4,
                    "job_description": "The Client Solutions Manager for Facebook s Global Marketing Solutions team is "
                                       "a strategic and enthusiastic solution-driver who puts our customers at the core"
                                       " of everything we do. This is an outstanding opportunity to build and manage "
                                       "key relationships, be a platform and product expert, and become an expert in "
                                       "media planning, strategy and measurement to our Fortune 500, multi-channel "
                                       "advertisers. With proven understanding of both online and traditional media, "
                                       "this role is responsible for partnering with the sales team to develop "
                                       "industry-specific relationships, drive revenue by negotiating and optimizing "
                                       "complex opportunities, and use data and analytics to build a consultative "
                                       "solution for our customers. The Client Solutions Manager will establish and "
                                       "strengthen key client relationships with a focus on driving revenue, advertiser"
                                       " education & advertiser satisfaction. Success in this position requires strong"
                                       " consultative sales, analytical, and technical skills, a focus on client "
                                       "service, and the ability to thrive in a dynamic, team-focused environment "
                                       "delivering against tight deadlines. This position is based in our NYC office.",
                    "job_id": 18,
                    "job_title": "Client Solutions Manager, Tech/Telco (NYC)",
                    "link": "https://www.facebook.com/careers/department?dept=sales&req=a0I1200000G4WKMEA3",
                    "location_id": 5
                },
                {
                    "company_id": 4,
                    "job_description": "Release Engineering plays an integral role in implementing and executing "
                                       "product release processes. The role supports Facebook s engineering by managing"
                                       " the source code management system, automating builds and regression testing, "
                                       "building tools and monitoring used in software deployments, and coordinating "
                                       "and pushing new releases to the production infrastructure. The Release "
                                       "Engineering team ensures that new software is released in a streamlined manner "
                                       "from development to production. The team establishes procedures and develops "
                                       "tools that are used by both the Engineering and Operations teams. As a Release "
                                       "Engineer you ll use your strong technical ability to drive product releases "
                                       "across many different systems and teams. You ll work hard to ensure that "
                                       "Facebook s products are delivered with a repeatable and scalable process.",
                    "job_id": 19,
                    "job_title": "Release Engineer",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0IA0000006cQOOMA2",
                    "location_id": 5
                },
                {
                    "company_id": 4,
                    "job_description": "Facebook is seeking an experienced Software Engineer to join our Infrastructure"
                                       " Engineering team in Boston. The position is full-time and is based in our "
                                       "Cambridge, MA office. There are minimal travel requirements for this position. "
                                       "Infrastructure Engineering builds large, distributed components that run "
                                       "Facebook. Our code serves millions of requests per second, and it does so with "
                                       "subsecond latency and in a fault tolerant manner. We handle everything from "
                                       "Facebook scale data storage, to synchronization and coordination of large "
                                       "server clusters, to providing a runtime environment for front end Facebook "
                                       "code. We are looking for candidates who share a passion for tackling complexity"
                                       " and building platforms that can scale through multiple orders of magnitude.",
                    "job_id": 20,
                    "job_title": "Software Engineer, Infrastructure",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0IA000000CxO6SMAV",
                    "location_id": 6
                },
                {
                    "company_id": 4,
                    "job_description": "Full Stack Web Developer WhatsApp is the world s largest and fastest growing "
                                       "communication company with over 600M Monthly active users globally. A Top 25 "
                                       "iOS app in more than 100 countries and an Android app with more than 500M "
                                       "installs on Google Play! Using your startup mindset and your experience "
                                       "developing native mobile apps, you will create new, awesome features used by "
                                       "600+ Million current WhatsApp users. We are looking for Software Web Developer "
                                       "Downtown Mountain View, CA",
                    "job_id": 21,
                    "job_title": "Full Stack Web Developer- Tools, WhatsApp",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0IA000000G41MfMAJ",
                    "location_id": 10
                },
                {
                    "company_id": 4,
                    "job_description": "Great virtual reality technology depends on advances in computer vision and "
                                       "tracking. As a computer vision engineer at Oculus, you ll be developing "
                                       "software for cutting edge vision applications that transform virtual reality "
                                       "from dream to reality. We re looking for a creative engineer to usher in the "
                                       "next era of human-computer interaction by integrating computer vision into "
                                       "everyday environments and practical products.",
                    "job_id": 22,
                    "job_title": "Computer Vision Engineer, Oculus",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0I1200000G4WSQEA3",
                    "location_id": 10
                },
                {
                    "company_id": 4,
                    "job_description": "Facebook s mission is to give people the power to share and make the world more"
                                       " open and connected. People use Facebook to stay connected with friends, "
                                       "family, & businesses, to discover what s going on in the world, and to share "
                                       "and express what matters to them. The Small & Medium Business (SMB) team "
                                       "contributes directly to Facebook s mission by connecting small businesses with "
                                       "their customers and helping them grow through solutions like pages and "
                                       "advertising. We succeed when we help our customers grow their business. The SMB"
                                       " team is seeking a data analyst who is passionate about using data and insights"
                                       " to drive business strategy, inform its execution, and improve efficiency. The "
                                       "analyst will focus on understanding the existing North America market and "
                                       "identifying future opportunities for growth. The ideal candidate is "
                                       "action-oriented and passionate about using data and analysis to evaluate "
                                       "success and inform efficiency in a fast-paced, dynamic environment. This is a "
                                       "full time position based in our Menlo Park HQ and will report to the Director "
                                       "of SMB North America.",
                    "job_id": 23,
                    "job_title": "Data Analyst, Small & Medium Business",
                    "link": "https://www.facebook.com/careers/department?dept=data&req=a0I1200000G4VqJEAV",
                    "location_id": 10
                },
                {
                    "company_id": 4,
                    "job_description": "Client Tools - Intern Downtown Mountain View, CA WhatsApp is the world s "
                                       "largest and fastest growing communications company with over 600M Monthly "
                                       "active users globally. A Top 25 iOS app in more than 100 countries and an "
                                       "Android app with more than 500M installs on Google Play! Using your startup "
                                       "mindset and your experience developing native mobile apps, you will create new,"
                                       " awesome features used by 600+ Million current WhatsApp users. We are looking "
                                       "for Mobile Software Developers for all our platforms: iOS, Android, Windows "
                                       "Phone, BlackBerry, and Nokia. We are seeking an intern to develop automations "
                                       "to capture screenshots from various WhatsApp applications to be published in "
                                       "our WhatsApp FAQ.",
                    "job_id": 24,
                    "job_title": "Client Tools (WhatsApp) Intern",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0I1200000G4V9MEAV",
                    "location_id": 10
                },
                {
                    "company_id": 4,
                    "job_description": "Facebook is seeking a Speech Recognition Research Scientist to join our "
                                       "research team in Menlo Park. The ideal candidate will have research experience "
                                       "developing speech recognition systems in different languages. Individuals in "
                                       "this role should be experts in acoustic modeling, including discriminative "
                                       "training, neural networks, and machine learning, and have experience working on"
                                       " large quantities of data. The candidate will help Facebook conduct research "
                                       "that support naturally spoken input in more than 70 languages.",
                    "job_id": 25,
                    "job_title": "Research Scientist, Speech Recognition/Acoustic Modeling",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0IA000000G2gDLMAZ",
                    "location_id": 10
                },
                {
                    "company_id": 4,
                    "job_description": "How would Facebook scale to the next billion users? The Infrastructure Strategy"
                                       " group is responsible for the strategic analysis to support and enable the "
                                       "continued growth critical to Facebook s infrastructure organization. The ideal"
                                       " candidate will be passionate about Facebook, highly analytical, have strong "
                                       "mathematical aptitude and has experience using data to drive cost effective "
                                       "decision making. This is a full-time position based in our headquarters in "
                                       "Menlo Park, CA.",
                    "job_id": 26,
                    "job_title": "Data Scientist, Infrastructure",
                    "link": "https://www.facebook.com/careers/department?dept=infrastructure&req=a0I1200000G4W3PEAV",
                    "location_id": 10
                },
                {
                    "company_id": 4,
                    "job_description": "Facebook is seeking an avid problem solver to join its infrastructure "
                                       "sustainability team to focus on data tracking and strategic analysis. The "
                                       "Sustainability Analyst will turn raw data into useful information, analyze "
                                       "operational impacts and contribute to strategic thinking about data impact and "
                                       "the projects it informs.",
                    "job_id": 27,
                    "job_title": "Sustainability Analyst",
                    "link": "https://www.facebook.com/careers/department?dept=infrastructure&req=a0I1200000G4WS1EAN",
                    "location_id": 10
                },
                {
                    "company_id": 4,
                    "job_description": "Do you like working with big data? Are you interested in working with some of "
                                       "the largest distributed distributed databases and data warehouses in the world?"
                                       " If yes, we want to talk to you. Facebook is seeking a Data Platform Engineer "
                                       "to join the Enterprise Data Infrastructure team to help our Facebook teams "
                                       "analyze multi-petabytes of data. You will help build and maintain solutions "
                                       "around the various Facebook distributed database technologies including "
                                       "HDFS/Hive, Presto, RocksDB, Scribe, and Vertica. The person should be creative "
                                       "and passionate about large scale, massively distributed, high performance "
                                       "distributed databases and data analysis tools. Their focus will enable the next"
                                       " generation of big data analysis platforms. This is a full time position at "
                                       "Facebook Menlo Park campus",
                    "job_id": 28,
                    "job_title": "Data Platform Engineer",
                    "link": "https://www.facebook.com/careers/department?dept=it&req=a0IA000000G42VUMAZ",
                    "location_id": 10
                },
                {
                    "company_id": 4,
                    "job_description": "Facebook is seeking a MySQL Database Engineer. This position will be primarily"
                                       " responsible for managing and providing active support for all aspects of the "
                                       "Facebook MySQL data set while helping to facilitate its continuous evolution "
                                       "from today s best in class to that of tomorrow. Candidates should have "
                                       "extensive experience in writing efficient automation software and a visceral "
                                       "aversion to doing the same task twice. Some of the things we are working on can"
                                       " be seen at facebook.com/MySQLatFacebook.",
                    "job_id": 29,
                    "job_title": "MySQL Database Engineer",
                    "link": "https://www.facebook.com/careers/department?dept=engineering&req=a0IA000000CxfUlMAJ",
                    "location_id": 10
                },
                {
                    "company_id": 5,
                    "job_description": "You will work on cutting-edge problem and participate in the engineering "
                                       "life-cycle at Twitter, including designing distributed systems, writing "
                                       "production code, conducting code reviews and working alongside our "
                                       "infrastructure and reliability teams. You will be equally comfortable doing "
                                       "incremental quality work and also building brand new systems to enable future "
                                       "quality improvements. ",
                    "job_id": 30,
                    "job_title": "Software Engineer - Machine Learning/Relevance (Seattle)",
                    "link": "https://about.twitter.com/careers/positions?jvi=op86Xfwk,Job&s=Indeed",
                    "location_id": 2
                },
                {
                    "company_id": 5,
                    "job_description": "Our engineering teams are responsible for the services and infrastructure "
                                       "that connect hundreds of millions of active Twitter users to real-time "
                                       "information about what s relevant in their lives and the world we live in. We "
                                       "work on some of the world s largest distributed systems -- our core "
                                       "infrastructure receives hundreds of millions of tweets per day and serves tens "
                                       "of billions of API requests, all with an uptime in excess of 99.9%. Our other "
                                       "systems operate at a similarly staggering scale: we serve over 2+ billion "
                                       "search queries per day, render hundreds of millions of ad impressions, and "
                                       "process hundreds of terabytes of log and interaction data daily. As a software "
                                       "engineer at Twitter, you will help us build, scale and maintain these systems, "
                                       "all of which have a direct impact on the lives of our users and the success of "
                                       "our business. ",
                    "job_id": 31,
                    "job_title": "Software Engineer - Systems (Seattle)",
                    "link": "https://about.twitter.com/careers/positions?jvi=o5ViZfw1,Job&s=Indeed",
                    "location_id": 2
                },
                {
                    "company_id": 5,
                    "job_description": "A Senior Developer ready to design and implement awesome new features through "
                                       "innovation and data-driven iterations at Twitter scale. Someone who wants to "
                                       "push limits of product innovation using the latest advancements in technology "
                                       "and methods - working closely with product managers, designers and other "
                                       "engineering teams. Someone that works best in an environment with a sense of "
                                       "urgency and can rapidly iterate on product/platform features.",
                    "job_id": 32,
                    "job_title": "Software Engineer - Product (Seattle)",
                    "link": "https://about.twitter.com/careers/positions?jvi=om76Xfwg,Job&s=Indeed",
                    "location_id": 2
                },
                {
                    "company_id": 5,
                    "job_description": "Brainstorm and implement products that improve the lives of all Twitter "
                                       "employees. Rapidly prototype new ideas with your teammates. Develop and "
                                       "maintain full stack web applications.",
                    "job_id": 33,
                    "job_title": "Software Engineer - Corporate Productivity",
                    "link": "https://about.twitter.com/careers/positions?jvi=ozXTZfw8,Job&s=Indeed",
                    "location_id": 3
                },
                {
                    "company_id": 5,
                    "job_description": "The Engineering Effectiveness team is empowered to build the engineering "
                                       "infrastructure, platform and tools to give Twitter this competitive edge. We "
                                       "design and develop the engineering infrastructure which is distributed, "
                                       "scalable, and enables fast iterations via continuous integration and reliable "
                                       "deployments.  Our contributions make Twitter Engineering an environment where "
                                       "developers thrive. This role will help shape Twitter s future on tools, "
                                       "infrastructure and methodologies for the massive scale we are trying to "
                                       "achieve.  If you have empathy for developers, passion for engineering "
                                       "productivity, experience delivering scalable distributed systems - you will "
                                       "find this role liberating and challenging.",
                    "job_id": 34,
                    "job_title": "Software Engineer - Engineering Effectiveness",
                    "link": "https://about.twitter.com/careers/positions?jvi=oQCqXfwz,Job&s=Indeed",
                    "location_id": 3
                },
                {
                    "company_id": 5,
                    "job_description": "To strengthen our growing team, we are looking for an experienced Salesforce "
                                       "Developer to design and build highly scalable business application solutions "
                                       "leveraging force.com, service cloud, sales cloud, and app exchange solutions. "
                                       "As an integral member of the IT business systems team, this position will be "
                                       "responsible for developing innovative solutions for business process "
                                       "automation. You will possess outstanding interpersonal skills and demonstrate "
                                       "yourself to be a great analytical thinker. You are team-oriented, and you "
                                       "thrive in a fast paced environment.",
                    "job_id": 35,
                    "job_title": "IT Applications Engineer",
                    "link": "https://about.twitter.com/careers/positions?jvi=oONQZfwa,Job&s=Indeed",
                    "location_id": 3
                },
                {
                    "company_id": 5,
                    "job_description": "Twitter is looking for great engineers to design and build our next generation "
                                       "of revenue products. You will be joining a team that is making a huge impact on"
                                       " Twitter s business and providing an indispensable platform for marketers. We "
                                       "work in small teams and ship to production every day. We re driven by "
                                       "measurement and data to inform our decisions, learning about our users and "
                                       "their problems. Our culture emphasizes creative problem solving, fast iteration"
                                       " and execution. Join us in our mission to build the world s highest-performing"
                                       " advertising platform that s also delightful to Twitter users. ",
                    "job_id": 36,
                    "job_title": "Software Engineer - Monetization",
                    "link": "https://about.twitter.com/careers/positions?jvi=oHAqXfwo,Job&s=Indeed",
                    "location_id": 3
                },
                {
                    "company_id": 5,
                    "job_description": "Create automated test scripts for iOS, Android, and web. Work closely alongside"
                                       " the API, Infrastructure, and Mobile teams. Documenting test cases, bug "
                                       "reporting,test execution  and reporting test status. Assure resolution of "
                                       "issues by following through to the end of the testing process. Document and "
                                       "execute regression, functional, and integration tests. Ensure the best possible"
                                       " experience for the users of Vine",
                    "job_id": 37,
                    "job_title": "QA Engineer-Vine",
                    "link": "https://about.twitter.com/careers/positions?jvi=oJCF0fwK,Job&s=Indeed",
                    "location_id": 5
                },
                {
                    "company_id": 5,
                    "job_description": "We are looking for a number of passionate, talented, entrepreneurial engineers "
                                       "to join the team in New York to help us build the foundations for our deep "
                                       "learning platform.",
                    "job_id": 38,
                    "job_title": "Software Engineer, Architecture (Twitter Cortex)",
                    "link": "https://about.twitter.com/careers/positions?jvi=ottA0fwg,Job&s=Indeed",
                    "location_id": 5
                },
                {
                    "company_id": 5,
                    "job_description": "Design, contribute and maintain efficient production code to an automated "
                                       "offline and online machine (deep) learning platform/service. Contribute to a "
                                       "mixed stack/full stack environment: the platform will include production "
                                       "backend code (scala), training jobs (lua, C, CUDA), web services and all the "
                                       "way to frontend code for live monitoring. Maintain a complex live system with "
                                       "production data dependencies, low-latency requirements. Work in a collaborative"
                                       " manner with team members in remote offices. Be awesome in developing JVM "
                                       "services (Scala, Java). Balance out your desire to ship code with your "
                                       "responsibility to get it right",
                    "job_id": 39,
                    "job_title": "Software Engineer, Systems (Twitter Cortex)",
                    "link": "https://about.twitter.com/careers/positions?jvi=ontA0fwa,Job&s=Indeed",
                    "location_id": 5
                },
                {
                    "company_id": 5,
                    "job_description": "We re looking for someone who shares our passion about cultivating and building"
                                       " an amazing user experience-- for all Fabric developers. Building relationships"
                                       " and maintaining the exceptional standard we have set as an organization is the"
                                       " focal point of the role. We pride ourselves that our ability to help our users"
                                       " is second to none.",
                    "job_id": 40,
                    "job_title": "Fabric Support Engineer",
                    "link": "https://about.twitter.com/careers/positions?jvi=o8pQZfw6,Job&s=Indeed",
                    "location_id": 6
                },
                {
                    "company_id": 5,
                    "job_description": "You will build web applications for our users, partners, and team. Those "
                                       "applications can range from business-critical internal tools to the core "
                                       "architecture of Twitter.com and our mobile website, with opportunities to work "
                                       "with a variety of languages and technologies.",
                    "job_id": 41,
                    "job_title": "Full Stack - Software Engineer (Boston)",
                    "link": "https://about.twitter.com/careers/positions?jvi=otBqXfwb,Job&s=Indeed",
                    "location_id": 6
                },
                {
                    "company_id": 6,
                    "job_description": "Lead technical customer pre-sales discussions/engagements as they relate to "
                                       "integration solutions with the LinkedIn Talent Solutions platform. Own and "
                                       "manage customer engagements through the entire implementation, delivery and "
                                       "support lifecycle. Manage technical partner relationships and continue to build"
                                       " on top of existing integrations and processes. Partner with different internal"
                                       " cross functional groups to communicate/escalate customer technical issues, "
                                       "help drive/influence product roadmap decisions based on customer/partner "
                                       "feedback, and implement internal tools/solutions to help demonstrate product "
                                       "value propositions. Develop and deliver on-going internal sales training and "
                                       "education of Talent Solutions products and services. Contribute to the "
                                       "development and sharing of best practices. Establish yourself as a Subject "
                                       "Matter Expert. Develop and maintain centralized content for customers, "
                                       "partners, and internal teams.",
                    "job_id": 42,
                    "job_title": "Technical Consultant, Customer Success",
                    "link": "http://www.ihispano.com/jobs/solutions-architect-technical-consulting?sk=1&id=8154e1e56662"
                            "93a6af5a00116d&utm_source=Indeed&utm_medium=cpc&utm_campaign=Indeed&rx_campaign=Indeed08&"
                            "rx_medium=cpc&rx_source=Indeed",
                    "location_id": 5
                },
                {
                    "company_id": 6,
                    "job_description": "As an Engineering Intern, you will join our SlideShare team in building a great"
                                       " site and excellent software. You will use Ruby and Puppet extensively but if "
                                       "you aren t familiar with these programs, no worries, we ll teach you! You will "
                                       "be responsible for dozens of code deployments per day which means you will ship"
                                       " code WHENEVER your feature is ready. Be prepared to ship on day one!",
                    "job_id": 43,
                    "job_title": "Engineering Intern",
                    "link": "http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Job&c=q2XaVfwO&j=oInx0fwm&s=Indeed",
                    "location_id": 9
                },
                {
                    "company_id": 6,
                    "job_description": "The Consumer Analytics team at LinkedIn works in close partnership with the "
                                       "Product team to identify opportunity to develop and enhance products and "
                                       "features that connect our Members with greater professional opportunity. We are"
                                       " looking for a Senior/Principal Data Scientist to join our team in developing "
                                       "innovative new technologies, features and products that will help further our "
                                       "mission of connecting the world s professionals. You will be responsible for "
                                       "informing strategy and decisions as well as building, measuring, understanding "
                                       "and improving products. Ultimately, you will develop data-driven product "
                                       "solutions that will add value to our customers and improve the professional "
                                       "lives of our members.",
                    "job_id": 44,
                    "job_title": "Principal Data Scientist, Consumer Analytics",
                    "link": "http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Job&c=qOW9Vfwy&j=ozHI0fwI&s=Indeed",
                    "location_id": 9
                },
                {
                    "company_id": 6,
                    "job_description": "Our goal is to build career navigation products that meets this challenge.  Our"
                                       " data at Linkedin is an embarrassment of riches.  Leveraging this data allows "
                                       "us to create experiences that allow members to explore, discover, understand "
                                       "and act upon ambitions and goals.  Above all, we seek to shift the world "
                                       "towards optimistic, determinate.",
                    "job_id": 45,
                    "job_title": "Product Innovation Intern",
                    "link": "http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Job&c=qOW9Vfwy&j=o1Cq0fwN&s=Indeed",
                    "location_id": 9
                },
                {
                    "company_id": 6,
                    "job_description": "The Business Analytics team is looking for data junkies who love turning data "
                                       "into gold and who want to make an impact. You will have the opportunity to help"
                                       " build data products and own analytics in the area of Mobile, Social "
                                       "Advertising, Engagement, etc. You will be working closely with monetization "
                                       "product managers and engineers to drive the business. LinkedIn s reputable "
                                       "internship program is known for plentiful activities and a fun Intern "
                                       "Hackathon. Join us this summer!",
                    "job_id": 46,
                    "job_title": "Product Analytics Intern",
                    "link": "http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Job&c=qOW9Vfwy&j=owDq0fwj&s=Indeed",
                    "location_id": 9
                },
                {
                    "company_id": 6,
                    "job_description": "LinkedIn member data is amazingly rich and provides a fantastic opportunity for"
                                       " Data Scientists to explore and create, ultimately developing ways for members "
                                       "to improve their professional lives. You ll have the opportunity to work with "
                                       "some of the best data people anywhere in an environment which truly values "
                                       "data-driven decisions.",
                    "job_id": 47,
                    "job_title": "Data Scientist, Growth Analytics",
                    "link": "http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Job&c=qOW9Vfwy&j=oPRz0fwZ&s=Indeed",
                    "location_id": 9
                },
                {
                    "company_id": 7,
                    "job_description": "This is a position in the Linux Technology Center, where we focus on Open "
                                       "Software Development. This position will be doing Software Defined Networking "
                                       "development on Docker, which requires experience in Linux Kernel Networking, "
                                       "open VSwitch, Linux Bonding, IPV6, and an overall broad exposure to networking."
                                       "Ready to change the way the world works? This is your chance to develop "
                                       "innovative new technology products, as well as your career, with the world s "
                                       "second largest software-maker. Hone your expertise alongside fellow talented "
                                       "professionals, where you ll develop some of the most exciting software "
                                       "solutions on the market. At IBM, we re strongly committed to the advancement of"
                                       " open Internet standards and applications as well.As an IBM Software Developer,"
                                       " you ll use the latest tools and technologies available to deliver state-of-the"
                                       "-art software. You ll be responsible for ensuring that company software "
                                       "components are expertly designed, tested, debugged, verified, and ready for "
                                       "integration into IBM s best-of-breed solutions that help organizations improve "
                                       "their business outcomes in the global marketplace.Required Bachelor s Degree At"
                                       " least 2 years experience in Networking Basic knowledge in LinuxBasic knowledge"
                                       " in Software Defined Networking At least 2 years experience in IPV6, "
                                       "Transmission Control Protocol/Internet Protocol (TCP/IP) Basic knowledge in "
                                       "Remote Direct Memory Access (RDMA)Basic knowledge in Virtualization Readiness "
                                       "to travel 10% travel annually English: FluentIBM is committed to creating a "
                                       "diverse environment and is proud to be an equal opportunity employer. All "
                                       "qualified applicants will receive consideration for employment without regard "
                                       "to race, color, religion, gender, gender identity or expression, sexual "
                                       "orientation, national origin, genetics, disability, age, or veteran status. IBM"
                                       " is also committed to compliance with all fair employment practices regarding "
                                       "citizenship and immigration status.",
                    "job_id": 48,
                    "job_title": "Software Developer ",
                    "link": "https://jobs3.netmedia1.com/cp/faces/job_summary?job_id=STG-0729637",
                    "location_id": 1
                },
                {
                    "company_id": 7,
                    "job_description": "Empowered. Innovative. Inspiring. Creative.The IBM Cloud Infrastructure "
                                       "Services team develops the products and services that will define the future of"
                                       " cloud. IBM builds the most innovative systems in our industry using the latest"
                                       " technology to deliver creative solutions that our customers depend on to "
                                       "succeed. You will be challenged to find creative and efficient ways to design "
                                       "products and services for our customers. If you are a developer who seeks "
                                       "responsibility, thrives when empowered, and wants to be a part of an agile team"
                                       " atmosphere; then look no further. You will be joining some of the most "
                                       "talented, creative, and dedicated developers. We strive to make this a place "
                                       "where you want to be, a place where you are proud to work, and where you are "
                                       "motivated to excel. Primary Responsibilities Design, develop and implement "
                                       "object oriented applications from prototype through implementation OpenStack "
                                       "experience, Virtualization, Cloud Computing Linux based development Java, "
                                       "Python, C Create highly scalable Service Oriented Architecture (SOA) / web "
                                       "services - Simple Object Access Protocol (SOAP), Representational State "
                                       "Transfer (REST), Extensible Markup Language ( XML-RPC), XML, JavaScript Object "
                                       "Notation (JSON) web services. Ideal Candidates Will Possess: Written and verbal"
                                       " communication skills Programming skills (for example: Java, Python, scripting,"
                                       " etc.) on different platforms Proven ability to work in a team environment "
                                       "Self-driven and able to work autonomously when necessary. Openings are for "
                                       "fulltime candidates. Prefer candidate to be located in commuting distance to "
                                       "Austin TX. Required Bachelor s Degree At least 3 years experience in relevant "
                                       "work At least 3 years experience in with Object Oriented (OO) programming "
                                       "languages and principles At least 1 year experience in leading an Agile team At"
                                       " least 6 months experience in Linux-based Development At least 6 months "
                                       "experience in virtualization technologies English: Fluent",
                    "job_id": 49,
                    "job_title": "Senior Cloud Developer",
                    "link": "https://jobs3.netmedia1.com/cp/faces/job_summary?job_id=GTS-0729042",
                    "location_id": 1
                },
                {
                    "company_id": 7,
                    "job_description": "Ready to change the way the world works? IBM Watson uses Cognitive Computing to"
                                       " tackle some of humanity s most challenging problems - like revolutionizing how"
                                       " doctors research cancer or transforming how businesses engage with their "
                                       "customers. We have an exciting opportunity for a Visual Designer. Technology "
                                       "should work for people, not the other way around. Watson s cognitive computing "
                                       "experiences represent a potential breakthrough in the ability of computers to "
                                       "become more humane, more helpful to people. Join the Watson Design team s "
                                       "mission to build revolutionary business and consumer applications that change "
                                       "the way people think and work in market areas such as Healthcare, Retail, "
                                       "Finance, Science, and more. Our environment is ever changing and requires a "
                                       "candidate who is flexible, thrives in ambiguity, and can collaborate across "
                                       "cross-functional groups and locations. We are looking for an experienced, "
                                       "hands-on Visual Designer with a passion for innovation, creativity, quality, "
                                       "and bringing new capabilities to market that delight and inspire users. "
                                       "Responsibilities:  Produce mood boards, storyboards, design briefs, visual "
                                       "language guidelines, visual compositions, and other artifacts required to "
                                       "develop and evolve user experience designs - Work with user experience "
                                       "designers, design researchers and developers to ensure visual design enhances "
                                       "the overall user experience - Work with Design Researchers to understand "
                                       "stakeholders, users and the markets in which they operate - Work with design "
                                       "team to lobby for and plan validation activities to ensure a delightful user "
                                       "experience. - Defend design choices using previous user research, heuristics "
                                       "and usability standards - Create world-class customer experiences and beautiful"
                                       " visuals that support and reinforce IBM Watson s vision, brand and business "
                                       "objectives across all platforms Key Skills: - Demonstrated ability to produce "
                                       "low-fidelity sketches and sleek, high fidelity visuals on tight schedules with "
                                       "a ton of initiative - Demonstrated knowledge of best practices in typography, "
                                       "color theory and iconography - Demonstrated ability to create click through "
                                       "prototypes to test and validate working hypothesis with users - Demonstrated "
                                       "ability to synthesize real user feedback into designs - Understanding of mobile"
                                       " and desktop graphic techniques and production practices - Working knowledge of"
                                       " how compositions translate to HTML, JavaScript and Cascading Style Sheets "
                                       "(CSS) used to deliver feasible designs - Knowledge of accessible designs - "
                                       "Ability to work with brand and design guidelines - Demonstrated written and "
                                       "verbal communication skills, including techniques to persuade and negotiate and"
                                       " the ability to articulate alternative approaches - Demonstrated storytelling "
                                       "and presentation skills - Attention to detail We live in a moment of remarkable"
                                       " change and opportunity. The convergence of data and technology is transforming"
                                       " industries, society and even the workplace. New roles are being created that"
                                       " never existed before to meet the demands of this transformation. And IBM "
                                       "Watson is now looking for talent to usher in the next era of cognitive "
                                       "computing. Embark on the journey with us at IBM Watson. Please attach your "
                                       "portfolio for consideration (URL or PDF). Find out more about Watson: "
                                       "http://www.ibm.com/smarterplanet/us/en/ibmwatson/ Required High School "
                                       "Diploma/GED At least 1 year experience in working in a collaborative team At "
                                       "least 1 year experience in customer-facing roles Readiness to travel 25% travel"
                                       " annually English: Fluent",
                    "job_id": 50,
                    "job_title": "Watson Visual Designer",
                    "link": "https://jobs3.netmedia1.com/cp/faces/job_summary?job_id=SWG-0729043",
                    "location_id": 5
                },
                {
                    "company_id": 7,
                    "job_description": "IBMiX Front End Developers: Participate in the design of client side "
                                       "engineering solutions Hand code web-based applications, web pages, emails, and"
                                       " web-based mobile experience Integrate your code with other technologies "
                                       "(Flash, Web Services, client back-end systems, content management systems, etc)"
                                       " Optimize performance of front-end applications Work with visual designers, "
                                       "interaction designers and software engineers Emulate existing html schemes and "
                                       "create new ones that will integrate well with existing HTML We think bigger "
                                       "than an agency and more creatively than a consultancy with the power to "
                                       "integrate the whole system. We are IBM Interactive Experience, 2014 Advertising"
                                       " Age s largest digital agency network in the world. We are a next generation "
                                       "services company dedicated to creating transformative ideas that get our "
                                       "clients to the future first. In this dynamic role, you will have the "
                                       "opportunity to interact directly with clients. As such, occasional travel to "
                                       "client sites may be required, up to 4 days per week. Required High School "
                                       "Diploma/GED At least 4 years experience in developing responsive front-end in a"
                                       " waterfall or agile engagement and working with AJAX and services/Application "
                                       "Programming Interfaces (APIs) to serve up dynamic and data-heavy content At "
                                       "least 4 years experience in working with AJAX and services and APIs to serve up"
                                       " dynamic and data-heavy content At least 4 years experience in integrating "
                                       "major third party APIs (Facebook Open Graph, Twitter, Google Maps, YouTube, "
                                       "Open Social, etc.) At least 4 years experience in Agency environment, working "
                                       "with visual and User Experience (UX) designers At least 4 years experience in "
                                       "hand coding At least 2 years experience in working within Model-View-Controller"
                                       " (MVC) frameworks At least 4 years experience in one or more of the following:"
                                       " Drupal, Joomla, Symfony, WordPress, AEM, Teamsite, Sitecore (or similar) At "
                                       "least 4 years experience in product and package selection methods Readiness to"
                                       " travel Up to 4 days a week (home on weekends-based on project requirements) "
                                       "English: Intermediate ",
                    "job_id": 51,
                    "job_title": "Senior Front-End Developer - IBM Interactive Experience",
                    "link": "https://oracle.taleo.net/careersection/2/jobdetail.ftl?job=87689",
                    "location_id": 5
                },
                {
                    "company_id": 7,
                    "job_description": "Software engineering role in San Francisco to maintain and enhance Tealeaf "
                                       "Replay capabilities. Tealeaf s products provide visibility into the customer "
                                       "experience by capturing, analyzing and replaying customers  visits from web "
                                       "sites or mobile applications. IBM Tealeaf Customer Experience Management "
                                       "enables organizations to deliver a leading-edge customer experience for their "
                                       "digital channels by providing demonstrated insight into the interactions of "
                                       "individual customers. It provides awareness of struggle trends, discovery of "
                                       "sources of experience friction and quantified business impact. Customer "
                                       "Experience Management s insights enable companies to answer the most "
                                       "compelling, yet difficult questions that plague marketing, merchandising, "
                                       "e-commerce and customer service departments. Skills - C/C++ or Java, server "
                                       "development - Knowledge of JavaScript - Demonstrated knowledge of Web "
                                       "protocols, Web technologies - Demonstrated communication and collaboration "
                                       "skills - Demonstrated analytical and problem solving skills Required Bachelor s"
                                       " Degree At least 6 months experience in Java English:Fluent ",
                    "job_id": 52,
                    "job_title": "Software Developer ",
                    "link": "https://jobs3.netmedia1.com/cp/faces/job_summary?job_id=SWG-0710500",
                    "location_id": 3
                },
                {
                    "company_id": 7,
                    "job_description": "Ready to change the way the world works? This is your chance to develop "
                                       "innovative new technology products, as well as your career, with the world s "
                                       "second largest software-maker. Hone your expertise alongside fellow talented "
                                       "professionals, where you ll develop some of the most exciting software "
                                       "solutions on the market. At IBM, we re strongly committed to the advancement of"
                                       " open Internet standards and applications as well. As an IBM Software "
                                       "Developer, you ll use the latest tools and technologies available to deliver "
                                       "state-of-the-art software. You ll be responsible for ensuring that company "
                                       "software components are expertly designed, tested, debugged, verified, and "
                                       "ready for integration into IBM s best-of-breed solutions that help "
                                       "organizations improve their business outcomes in the global marketplace. Join "
                                       "us. Required Bachelor s Degree Basic knowledge in UI ( User Interface) "
                                       "Development and/or test Basic knowledge in Open Source tools Basic knowledge in"
                                       " UI ( User Interface) technologies such as HTML, CSS, JavaScript, etc. Basic "
                                       "knowledge in of databases and/or Selenium framework English: Fluent ",
                    "job_id": 53,
                    "job_title": "IBM Tealeaf - Entry Level Software Quality Assurance Engineer",
                    "link": "https://jobs3.netmedia1.com/cp/faces/job_summary?job_id=SWG-0699115",
                    "location_id": 3
                },
                {
                    "company_id": 7,
                    "job_description": "IBM is looking for smart, motivated developers with one or more years of "
                                       "experience in open source projects like Apache Hadoop, Spark, Yarn, Tachyon to "
                                       "become part of their Spark Center of Excellence. Candidate should have a "
                                       "demonstrated understanding of one or more of system design, distributed "
                                       "processing, memory based file systems, security. Demonstrated knowledge of Java"
                                       " / Scala as well as Java Virtual Machine (JVM) optimization is essential. "
                                       "Candidates should be able to pick up one or more new frameworks in short order "
                                       "as well as react to evolving technology landscape. Open source contributors:"
                                       " Send us your Github id! LI-BJ1 Required Bachelor s Degree At least 1 year "
                                       "experience in Java Programming At least 1 year experience in Apache Hadoop "
                                       "Programming English: Fluent ",
                    "job_id": 54,
                    "job_title": "Spark Kernel Developer / Committer ",
                    "link": "https://jobs3.netmedia1.com/cp/faces/job_summary?job_id=SWG-0719345",
                    "location_id": 8
                },
                {
                    "company_id": 7,
                    "job_description": "Reliability, Availability, and Serviceability (RAS) team is looking for a co-op"
                                       " to help work on the service/maintenance/repair graphical user interface for "
                                       "our next version of the DS8000. We re looking for candidates with proven Java "
                                       "skills, the ability to work on their own, and the drive to come learn about "
                                       "industry and business while working towards their degree. Required High School "
                                       "Diploma/GED At least 1 year experience in Java Programming At least 6 months "
                                       "experience in data structures in C/C++ or Java Basic knowledge in computer "
                                       "systems architecture Basic knowledge in Linux or Unix administration At least 2"
                                       " years experience in use programming languages English: Fluent ",
                    "job_id": 55,
                    "job_title": "Software Developer Co-Op",
                    "link": "https://jobs3.netmedia1.com/cp/faces/job_summary?job_id=STG-0718523",
                    "location_id": 8
                },
                {
                    "company_id": 7,
                    "job_description": "IBM is looking for an Information Technology Services - Developer who performs "
                                       "moderately complex application development in the design, development, "
                                       "analysis, implementation/integration and testing of moderately complex "
                                       "programming systems supporting key business activities. They will design, code,"
                                       " test, and provide ongoing support of an application or an application "
                                       "component. This role considers performance, serviceability, usability and "
                                       "maintainability while performing application development tasks. The Developer "
                                       "defines, researches, integrates or develops, releases, and maintains reusable "
                                       "application components on one or more platforms with proven technologies. This "
                                       "role solves problems based on precedent and procedures and follows standard "
                                       "application development methodology. Required Bachelor s Degree Basic knowledge"
                                       " in C++ Basic knowledge in Unix and/ or Linux Basic knowledge in Oracle Basic "
                                       "knowledge in WebSphere Basic knowledge in DB2 Basic knowledge in Java 2 "
                                       "Platform, Enterprise Edition (J2EE) Basic knowledge in Structured Query "
                                       "Language (SQL) Basic knowledge in Javascript Basic knowledge in JavaServer "
                                       "Pages (JSP) Basic knowledge in Analytical & Problem Solving English: Basic "
                                       "knowledge ",
                    "job_id": 56,
                    "job_title": "Information Technology Services - Developer ",
                    "link": "https://jobs3.netmedia1.com/cp/faces/job_summary?job_id=GBS-0719916",
                    "location_id": 7
                },
                {
                    "company_id": 7,
                    "job_description": "Empowered. Innovative. Inspiring. Creative. Intense. These are all words we use"
                                       " to describe life at SoftLayer. The Systems Development team develops the "
                                       "products and services that will define the future of cloud in the hosting "
                                       "industry. We build the most innovative systems in our industry using the latest"
                                       " technology to deliver creative solutions that our customers depend on to "
                                       "succeed. As a software engineer you will work on projects that push the limits "
                                       "of what is available to customers. For SoftLayer, automation is the key to "
                                       "success. You will be challenged to find creative and efficient ways to deploy "
                                       "products and services to our customers. If you are an impassioned developer who"
                                       " seeks responsibility, thrives when empowered, and wants to be a part of an "
                                       "agile team atmosphere; then look no further. You will be joining some of the "
                                       "most talented, creative, and dedicated developers. We strive to make SoftLayer "
                                       "a place where you want to be, a place where you are proud to work, and where "
                                       "you are motivated to excel. Primary Responsibilities - Design and develop "
                                       "innovative, company and industry impacting products and services - Design, "
                                       "develop and implement object oriented applications from prototype through "
                                       "implementation - Integrate open source and commercial enterprise applications "
                                       "into a publicly exposed API and web-based portal - Create highly scalable and "
                                       "performant Service Oriented Architecture (SOA) / web services - Simple Object "
                                       "Access Protocol (SOAP), Representational State Transfer (REST), Extensible "
                                       "Markup Language ( XML-RPC), XML, JavaScript Object Notation (JSON) web services"
                                       " - Take ownership and manage projects that vary in size and scope depending on "
                                       "requirements Required Skills - Demonstrated knowledge of 1 or more Object "
                                       "Oriented Programming (OOP) language such as Hypertext Preprocessor (PHP5+), "
                                       "C/C++, or Java - Demonstrated knowledge of Service Oriented Architecture (SOA) "
                                       "/ web services - Simple Object Access Protocol (SOAP), Representational State "
                                       "Transfer (REST), Extensible Markup Language ( XML-RPC), XML, JavaScript Object "
                                       "Notation (JSON) - 5+ years relevant work experience - Demonstrated knowledge of"
                                       " Model View Controller (MVC) architecture and implementation - Demonstrated "
                                       "understanding of object oriented design principles and patterns - Experience "
                                       "with relational databases and Structured Query Language - SQL (Oracle, MySQL, "
                                       "PostgreSQL) - A positive attitude and willingness drive projects to completion "
                                       "in a fast paced environment - Experience in large systems software design and "
                                       "development - Proven knowledge of Unix/Linux Additional Desired Qualifications:"
                                       " - Experience with unit testing (PHPUnit) - Experience using a framework such "
                                       "as CodeIgniter, Symfony, or Zend - Experience using an ORM (Doctrine, Propel, "
                                       "Hibernate)",
                    "job_id": 57,
                    "job_title": "SoftLayer Software Engineer - Networking ",
                    "link": "https://jobs3.netmedia1.com/cp/faces/job_summary?job_id=GTS-0724169",
                    "location_id": 7
                },
                {
                    "company_id": 8,
                    "job_description": "Come join the Product Infrastructure Team and you ll make Carousel, Mailbox and"
                                       " future Dropbox apps amazing. Responsibilities Build cross-platform C++, "
                                       "Objective-C and Java libraries to support core features across all our mobile "
                                       "and desktop apps Refactor our codebase to maximize cross-team sharing and "
                                       "extract the core to be reused across teams Find scalable ways to increase "
                                       "development speed and overall code quality through better APIs, tools, or magic"
                                       " Review code and teach others great software design practices Make Dropbox the "
                                       "best place to build apps Requirements Experience writing libraries or "
                                       "frameworks in either Java, Objective C, or C++11/14 (multiple is a plus) "
                                       "Experience with at least one mobile platform (is a strong plus) or a desire to "
                                       "learn Great intuition for software design - clean interfaces and well-layered "
                                       "systems using your language of choice Experience with large scale development "
                                       "Experience with physical and logical code organization for cross-team code "
                                       "sharing (is a strong plus) Passion for clean, simple, well-documented, "
                                       "well-tested, and well-designed code Strong ownership and drive to improve "
                                       "codebase Communicate technical ideas to others",
                    "job_id": 58,
                    "job_title": "Software Engineer - Mobile Product Infrastructure",
                    "link": "https://www.dropbox.com/jobs/listing/535?ds=4f70cc000a",
                    "location_id": 3
                },
                {
                    "company_id": 10,
                    "job_description": "Responsibilities: Maintain existing and future custom application code and "
                                       "configuration Regularly interface with developers and team members for capacity"
                                       " and architecture planning Make recommendations for improvements to existing "
                                       "architecture Participate in regular deployments of code updates Other tasks as "
                                       "assigned Requirements: Undergraduate degree in Computer Science or similar work"
                                       " experience At least 2 years of proven hands-on experience deploying and "
                                       "maintaining complex, custom, multi-tiered application systems in a complex, "
                                       "global, online operations group Experience with JAVA applications in a Tomcat "
                                       "environment strongly preferred Experience with provisioning and configuration "
                                       "management tools and technologies such as Puppet, Rundeck, kickstart, and "
                                       "others strongly preferred At least 4 years of experience with Linux as a power "
                                       "user or administrator Strong scripting skills in PERL and others Ability to "
                                       "research technical problems and solutions online Interest in learning and "
                                       "taking on increasingly complex tasks Strong organizational skills and detail-"
                                       "oriented work ethic Willingness to work flexible / odd hours at times, based on"
                                       " needs, including on-call rotation",
                    "job_id": 74,
                    "job_title": "DevOps Engineer ",
                    "link": "http://www.indeed.com/viewjob?jk=13dd311f0f636f63&q=company%3Aindeed+developer&tk=19gsvnbu"
                            "v19vi04t",
                    "location_id": 1
                },
                {
                    "company_id": 8,
                    "job_description": " At the heart of Dropbox lies the largest networked filesystem in history. We "
                                       "routinely tackle audacious challenges, often against competitors who have "
                                       "10-50x our resources. On top of this foundation, we re creating products that "
                                       "enable people to do amazing things with their stuff across all their devices. "
                                       "Responsibilities Build infrastructure to manage metadata for hundreds of "
                                       "billions of files, hundreds of petabytes of user data, and millions of "
                                       "concurrent connections Create a platform that is the fabric connecting over "
                                       "300,000 of the world s apps, devices, and services; redefine sync for a mobile "
                                       "era (see the inaugural DBX conference for more) Relentlessly measure and "
                                       "optimize, and build one of industry s most advanced analytics platforms to "
                                       "derive meaning from vast amounts of data Craft the data and networking layers "
                                       "that enable rapid product innovation across Android, iOS, and mobile web Push "
                                       "the boundaries of OS integration on Mac, Windows, Android, iOS, and Linux. For "
                                       "example, on OS X we had to reverse-engineer the Finder to show current file "
                                       "sync status, and on Android and iOS we ve optimized JSON parsing and have built"
                                       " custom bitmap caches to present lightning-fast views of tens of thousands of "
                                       "photos. Enable our users to store and share billions of memories on Dropbox, "
                                       "and make these experiences delightful, from our mobile photo uploaders and web "
                                       "albums to a host of exciting features that will launch over the next few months"
                                       " Help millions of businesses around the world who run on Dropbox, from your "
                                       "neighborhood corner store all the way up to Fortune 500 companies; build "
                                       "Dropbox for Business to help teams be more productive and collaborative "
                                       "Reinvent email with Mailbox, a mobile-first inbox that helps people focus and "
                                       "simplify their lives even more",
                    "job_id": 59,
                    "job_title": "Software Engineer - University Grad",
                    "link": "https://www.dropbox.com/jobs/listing/145?ds=4f70cc000a",
                    "location_id": 3
                },
                {
                    "company_id": 8,
                    "job_description": "Our engineering team is passionate about building awesome products at massive "
                                       "scale. We ve developed a set of values that enables us to do this. "
                                       "Specifically, we write great software and sweat the details, relentlessly focus"
                                       " on impact, and create a collaborative culture. Creating elegant products "
                                       "begins with lots of prototyping and iteration to explore the problem space. It "
                                       "culminates in careful attention to edge cases and error handling, polished "
                                       "code, and great tests to ensure that we ship a reliable product that never "
                                       "compromises data integrity or security. Every Dropbox software release improves"
                                       " millions of lives, and you ll find a high petabyte-to-engineer ratio here. "
                                       "We re all about shipping high-leverage projects, even if they re risky or "
                                       "novel. We care deeply about collaboration, feedback, and iteration. Trust and "
                                       "respect are deeply rooted in our engineering culture. Responsibilities Build "
                                       "infrastructure to manage metadata for hundreds of billions of files, hundreds "
                                       "of petabytes of user data, and millions of concurrent connections Create a "
                                       "platform that is the fabric connecting over 300,000 of the world s apps, "
                                       "devices, and services; redefine sync for a mobile era (see the inaugural DBX "
                                       "conference for more) Relentlessly measure and optimize, and build one of "
                                       "industry s most advanced analytics platforms to derive meaning from vast "
                                       "amounts of data Craft the data and networking layers that enable rapid product"
                                       " innovation across Android, iOS, and mobile web Push the boundaries of OS "
                                       "integration on Mac, Windows, Android, iOS, and Linux. For example, on OS X we "
                                       "had to reverse-engineer the Finder to show current file sync status, and on "
                                       "Android and iOS we ve optimized JSON parsing and have built custom bitmap "
                                       "caches to present lightning-fast views of tens of thousands of photos. Enable "
                                       "our users to store and share billions of memories on Dropbox, and make these "
                                       "experiences delightful, from our mobile photo uploaders and web albums to a "
                                       "host of exciting features that will launch over the next few months Help "
                                       "millions of businesses around the world who run on Dropbox, from your "
                                       "neighborhood corner store all the way up to Fortune 500 companies; build "
                                       "Dropbox for Business to help teams be more productive and collaborative "
                                       "Reinvent email with Mailbox, a mobile-first inbox that helps people focus and "
                                       "simplify their lives even more",
                    "job_id": 60,
                    "job_title": "Software Engineer - University Grad - New York",
                    "link": "https://www.dropbox.com/jobs/listing/849?ds=4f70cc000a",
                    "location_id": 5
                },
                {
                    "company_id": 8,
                    "job_description": "Responsibilities We re building infrastructure to manage metadata for hundreds "
                                       "of billions of files, hundreds of petabytes of user data, and millions of "
                                       "concurrent connections. The Dropbox Platform is the fabric connecting over 100 "
                                       "thousand of the world s apps, devices, and services. Our team is redefining "
                                       "sync for a mobile era. (See the inaugural DBX conference for more.) We "
                                       "relentlessly measure and optimize, and we re building one of industry s most "
                                       "advanced analytics platforms to derive meaning from vast amounts of data. Our "
                                       "core mobile team crafts the data and networking layers that enable rapid "
                                       "product innovation across Android, iOS, and mobile web. Our lightweight clients"
                                       " push the boundaries of OS integration on Mac, Windows, Android, iOS, and "
                                       "Linux. For example, on OS X we had to reverse-engineer the Finder to show "
                                       "current file sync status, and on Android and iOS we ve optimized JSON parsing "
                                       "and have built custom bitmap caches to present lightning-fast views of tens of "
                                       "thousands of photos. People store and share billions of memories on Dropbox, "
                                       "and we love making these experiences delightful, from our mobile photo "
                                       "uploaders and web albums to a host of exciting features that will launch over "
                                       "the next few months. Millions of businesses around the world run on Dropbox, "
                                       "from your neighborhood corner store all the way up to Fortune 500 companies. "
                                       "We re building Dropbox for Business to help teams be more productive and "
                                       "collaborative. We re reinventing email with Mailbox, a mobile-first inbox that "
                                       "helps people focus and simplify their lives even more.",
                    "job_id": 61,
                    "job_title": "Software Engineer - Seattle",
                    "link": "https://www.dropbox.com/jobs/listing/661?ds=4f70cc000a",
                    "location_id": 2
                },
                {
                    "company_id": 8,
                    "job_description": "Requirements Great engineering skills and strong CS fundamentals Ability to "
                                       "work both independently and in cooperation with others A sense of urgency and "
                                       "ownership over the product Comfortable with full-stack projects and able to "
                                       "build a minimum working product quickly Good product sense and eagerness to "
                                       "work on a diverse set of engineering challenges Fluency with both front-end "
                                       "(e.g., html/css/javascript, iOS, Android, etc.) and back-end technologies -- "
                                       "however specific technologies don t matter nearly as much as having a breadth "
                                       "of experience and an eye for great product Thrives in open or ambiguous "
                                       "environments Great attitude towards work and people Intellectually curious, "
                                       "passionate, and inventive Focus on quality, sweat the details, and delight our "
                                       "users",
                    "job_id": 62,
                    "job_title": "Software Engineer - Product",
                    "link": "https://www.dropbox.com/jobs/listing/491?ds=4f70cc000a",
                    "location_id": 3
                },
                {
                    "company_id": 9,
                    "job_description": "Internal Infrastructure: Ten data centers around the globe with several hundred"
                                       " thousand servers that all need to seamlessly interact like one of your LAN "
                                       "parties back in college. If you like HUGE environments then jump on into this "
                                       "playground. Powershell DSCAnsible, Chef, Puppet, Salt and whatever comes next. "
                                       "See what the Rackspace teams are doing for our customers. MapMyFitness Story "
                                       "Job Responsibilities In this role you will: Support customers and internal "
                                       "teams on an as-needed basis Collaborate with other teams on tools for systems "
                                       "automation Work in conjunction with multiple teams to make sure that the "
                                       "infrastructure and customer applications work harmoniously together "
                                       "Qualifications Required Qualifications: Windows Server OS knowledge, including "
                                       "Active Directory, Server Deployment, and High-Availability Familiarity with Web"
                                       " programming (.NET preferred) Familiarity with Powershell scripting 3+ years  "
                                       "experience as either a .NET software developer and/or Windows systems "
                                       "administrator with at least 1 year of current experience working with a "
                                       "high-traffic site Experience with high-availability, high-performance, open "
                                       "source web technologies General knowledge and understanding of Cloud-based "
                                       "systems architecture. High school diploma or equivalent required",
                    "job_id": 63,
                    "job_title": "DevOps Engineer I - Windows",
                    "link": "https://uscareers-rackspace.icims.com/jobs/13053/devops-engineer-i---windows/job?mode=job&"
                            "iis=Job+Board+-+Indeed.com&iisn=Indeed.com",
                    "location_id": 1
                },
                {
                    "company_id": 9,
                    "job_description": "Looking for more responsibility, how about these?: You ll be responsible for "
                                       "complex architectural design and development of hardware, software and "
                                       "networking systems. Analyzes systems and determines business requirements. Be "
                                       "ready for on-call duties as needed, because we like uptime! Ensures "
                                       "completeness and compatibility of the technical infrastructure to support "
                                       "system performance. Requires leading-edge skills in the latest areas of new "
                                       "technology. Mentors junior level engineers or administrators, and demonstrates "
                                       "the ability to own large subsystems with a high degree of accountability. "
                                       "Assists Manager to identify gaps in training and process. Review and approve "
                                       "technical documentation. You ll have to be able to diagnose and fix the most "
                                       "complex server and system-wide issues. Qualifications The ideal candidate will "
                                       "have the following: Requires six plus years of information systems "
                                       "design/architecture experience with a minimum of 3-4 years working in a cloud "
                                       "environment or equivalent customer support workplace. Excellent technical "
                                       "knowledge in methodologies, design, and implementation. Excellent analytical "
                                       "and design skills at multi-product/multi-environment level. Aware of business "
                                       "issues as they impact overall project plans. Strong communication and "
                                       "interpersonal skills. Able to resolve problems in a timely manner. Bachelor s "
                                       "degree in computer science or equivalent experience. RHCE certification or "
                                       "equivalent experience is required. Technology you ll need to be familiar with: "
                                       "Advanced Knowledge of Linux internals, configuration management, CI/CD, "
                                       "authentication/directory services, backups, caching, SSL, HA, load balancing, "
                                       "networking, application/performance monitoring, provisioning, and "
                                       "virtualization. Must be fluent in advanced scripting languages like Bash, "
                                       "Python (esp Ansible), and Ruby (esp. Puppet/Chef). Experience working with Java"
                                       " applications, the JVM, and Java servlet containers like Tomcat would be a "
                                       "plus. Prior experience with the common test frameworks such as unittest, rspec,"
                                       " serverspec, chefspec, kitchen-ci, puppet-rspec, beaker is a plus.",
                    "job_id": 64,
                    "job_title": "Linux Systems Engineer III",
                    "link": "https://uscareers-rackspace.icims.com/jobs/12831/linux-systems-engineer-iii/job?mode=job&"
                            "iis=Job+Board+-+Indeed.com&iisn=Indeed.com",
                    "location_id": 1
                },
                {
                    "company_id": 9,
                    "job_description": "What You ll Do Write excellent, fully-tested code in Node.js, Java and C "
                                       "Provide in-depth and always-improving code reviews to your teammates Fix things"
                                       " before they break Thoughtfully prioritize your work Troubleshoot and support"
                                       " production, addressing technical debt to improve sustainability Use an "
                                       "open-source collaborative development model, branching for each major feature, "
                                       "writing clear commit messages and PR descriptions Implement product features "
                                       "and refine specifications with Product & Project Managers Resolve operational "
                                       "issues by collaborating with upstream support groups and other engineering "
                                       "teams Qualifications Desired Qualities Strong CS fundamentals Skilled with at "
                                       "least one of C, Java, or Node.js Experience building and operating distributed "
                                       "systems A working knowledge of Linux internals Experience operating production "
                                       "systems Appreciation of modular software design and API Design Experience "
                                       "contributing to open-source projects ",
                    "job_id": 65,
                    "job_title": "Software Developer, Cloud Monitoring",
                    "link": "https://uscareers-rackspace.icims.com/jobs/13182/software-developer%3a-cloud-monitoring/"
                            "job?mode=job&iis=Job+Board+-+Indeed.com&iisn=Indeed.com",
                    "location_id": 3
                },
                {
                    "company_id": 9,
                    "job_description": " KNOWLEDGE/SKILLS/ABILITY: Advanced knowledge in multiple technologies relevant"
                                       " to current activities in the business unit. Advanced working knowledge of most"
                                       " technologies relevant to our core business. Demonstrates a systematic "
                                       "structured problem solving approach. Ability to generalize a specific problem "
                                       "and derive solution for a class of problem. Ability to derive causal "
                                       "relationship from ambiguous data. - JOB COMPLEXITY: Designs robust, scalable, "
                                       "secure, and globalized feature. Demonstrates sound rationale in making design "
                                       "trade-offs for various feature areas. Identifies risks and mitigation for "
                                       "various feature areas. Effectively manages dependencies for various feature "
                                       "areas. Drives continuous adoption and integration of relevant new technologies "
                                       "into design. Efficiently implements feature area with minimal technical debt. "
                                       "Feature areas are easy to deploy and maintainable. Proactively drives "
                                       "refactoring and code-reuse. Feature areas are bug free. Includes unit tests for"
                                       " feature areas to achieve established code coverage targets. Feature areas are "
                                       "test-driven designed, enabling efficient regression testing. Makes regular "
                                       "contribution to test automation. Evolves feature area(s) with new ideas to "
                                       "realize greater benefits or to solve newly anticipated problems. Focuses on "
                                       "multiple feature areas or components. Consistently, contributes to key "
                                       "functionalities for our product and service offering. - SUPERVISION: Works "
                                       "autonomously. Provides technical leadership and guidance to colleagues who are "
                                       "unfamiliar with own feature areas. Uses own growth experience to mentor "
                                       "developing colleagues. Qualifications - EXPERIENCE/EDUCATION: High school "
                                       "diploma or equivalent required. Bachelor s degree in a technology related field"
                                       " required. At the manager s discretion, additional relevant experience may "
                                       "substitute for the degree requirement. Typically requires 6-9 years of "
                                       "experience in software development, engineering, testing, or a related field. "
                                       "Solid software engineering fundamentals gained through training, course work or"
                                       " relevant experience. - PHYSICAL DEMANDS: General office environment. May "
                                       "require long periods sitting and viewing a computer monitor. Moderate levels of"
                                       " stress may occur at times. No special physical demands required.",
                    "job_id": 66,
                    "job_title": "Software Developer, VMware Cloud Practice",
                    "link": "https://uscareers-rackspace.icims.com/jobs/11691/software-developer%2c-vmware-cloud-"
                            "practice/job?mode=job&iis=Job+Board+-+Indeed.com&iisn=Indeed.com",
                    "location_id": 3
                },
                {
                    "company_id": 9,
                    "job_description": "In this role you will: Write lots of Python Work on all parts of the platform, "
                                       "front end, back end, automation, you name it Automate and innovate new ways to "
                                       "manage large database clusters Push the limits of MongoDB, then blog about it "
                                       "Work with cutting edge technology in the cloud computing space Provide "
                                       "Fanatical Support to our customers Create a sustainable and maintainable "
                                       "platform Install, configure, update and troubleshoot a HUGE MongoDB environment"
                                       " Collaborate with Engineers and System Administrators on technical issues Be "
                                       "part of the community. Attend conferences and meetups Qualifications 3+ years "
                                       "of Python development experience Strong HTML, CSS, and JavaScript skills, "
                                       "including JQuery Experience with multiple development languages (Ruby, PHP, "
                                       "Java, C++, etc...) Experience with agile-like development processes, including "
                                       "continuous integration strategies Strong understanding of git branching and "
                                       "merging flows Familiarity with Flask, Jinja2, and PyMongo Familiarity with "
                                       "vagrant, chef, puppet, fabric Good DevOps chops. Can run a system not just "
                                       "develop one Working knowledge of MongoDB or other open source database "
                                       "Extensive knowledge of Linux/Unix Fast learner, creative thinker, problem "
                                       "solver Team player, highly motivated and self-manageable Responsible, dedicated"
                                       " and responsive in non-working hours as needed Excellent interpersonal and "
                                       "communication skills Comfortable with collaborative tools such as IRC, wikis "
                                       "and basic ticket tracking systems Action and detail oriented. Highly motivated "
                                       "to drive projects to completion",
                    "job_id": 67,
                    "job_title": "Software Developer ObjectRocket",
                    "link": "https://uscareers-rackspace.icims.com/jobs/8999/software-developer-objectrocket/job?mode="
                            "job&iis=Job+Board+-+Indeed.com&iisn=Indeed.com&mobile=false&width=960&height=500&bga=true&"
                            "needsRedirect=false&jan1offset=-360&jun1offset=-300",
                    "location_id": 1
                },
                {
                    "company_id": 9,
                    "job_description": "In this role you will: Manage and maintain thousands of production customer "
                                       "databases Automate and innovate new ways to manage large database clusters Push"
                                       " the limits of MongoDB or MySQL, then blog about it Work with cutting edge "
                                       "technology in the cloud computing space Provide Fanatical Support to Rackers "
                                       "and our customers through innovative solutions Create sustainable and "
                                       "maintainable environments Install, configure, update and troubleshoot a HUGE "
                                       "MongoDB or MySQL environment Collaborate with Engineers and System "
                                       "Administrators on technical issues Be part of the community. Attend conferences"
                                       " and meetups Qualifications Position Requirements & Experience: 1+ year "
                                       "experience with MongoDB or MySQL in a production environment 2+ years managing"
                                       " highly available production systems Proficiency with Python, Perl, shell or "
                                       "other languages Extensive knowledge of Linux/Unix Fast learner, creative "
                                       "thinker, problem solver Team player, highly motivated and self-manageable "
                                       "Responsible, dedicated and responsive in non-working hours as needed Excellent "
                                       "interpersonal and communication skills Comfortable with collaborative tools "
                                       "such as IRC, wikis and basic ticket tracking systems Action and detail "
                                       "oriented. Highly motivated to drive projects to completion",
                    "job_id": 68,
                    "job_title": "Senior Database Administrator",
                    "link": "https://uscareers-rackspace.icims.com/jobs/9847/senior-database-administrator/job?mode=job"
                            "&iis=Job+Board+-+Indeed.com&iisn=Indeed.com",
                    "location_id": 1
                },
                {
                    "company_id": 9,
                    "job_description": "We are seeking a Mid-to-Senior level Python Developer to join our Engineering "
                                       "team to work on our scalable, highly-available MongoDB Database as a Service "
                                       "platform. Love a challenge? Anyone can manage a single application - we manage "
                                       "and maintain thousands of production databases supporting billions of "
                                       "operations. You ll be part of a highly capable and motivated team working on "
                                       "solving the hard problems of scalability, availability, and performance on a "
                                       "global platform. Qualifications Strong Python Development experience with "
                                       "agile-like development processes, including continuous integration strategies "
                                       "Knowledge of MongoDB or other open source database Knowledge of Linux/Unix Fast"
                                       " learner, creative thinker, problem solver Team player, highly motivated and "
                                       "self-manageable Responsible, dedicated and responsive in non-working hours as "
                                       "needed Excellent interpersonal and communication skills Comfortable with "
                                       "collaborative tools such as IRC, wikis and basic ticket tracking systems Action"
                                       " and detail oriented. Highly motivated to drive projects to completion Nice to "
                                       "Have: Prior experience with production large-scale distributed systems "
                                       "Demonstrated ability to work with a large amount of independence and "
                                       "responsibility Ability to work closely with information retrieval/machine "
                                       "learning experts on big-data problems. Some interest and familiarity with IR/ML"
                                       " is a plus, but it will not be your primary focus Prior experience with Lucene,"
                                       " ElasticSearch, Hadoop/mrjob, or large data stores (MySQL or NoSQL - we just "
                                       "want the right solution for the situation) A hunger for tracking down root "
                                       "causes -- no matter how deep it takes you -- and fixing them in systematic ways"
                                       " BA/BS degree in Computer Science, Math, or related degree",
                    "job_id": 69,
                    "job_title": "Python Developer",
                    "link": "https://uscareers-rackspace.icims.com/jobs/11849/application-administrator-i/job?mode=job&"
                            "iis=Job+Board+-+Indeed.com&iisn=Indeed.com",
                    "location_id": 1
                },
                {
                    "company_id": 9,
                    "job_description": "Overview & Responsibilities The Cloud Platform group in Rackspace is seeking a "
                                       "Python Software Developer to join its Servermill engineering team. Servermill "
                                       "is a mission critical application that enables support organization to deliver "
                                       "fanatical customer support to its customers. It automates workflow and other "
                                       "system administrator tasks like post server build processing, monitoring alerts"
                                       " etc. Responsibilities * Design and implement production grade software at "
                                       "cloud scale * Partner with QE/Test, Support, Operations and Product management "
                                       "to ensure high quality software releases per schedule * Evaluate technical "
                                       "aspects of other developer s designs and proposals * Provide estimates for "
                                       "development effort Qualifications The ideal candidate will have the following "
                                       "characteristics: * 5+ years of experience in software product development "
                                       "(design, coding, system engineering, object oriented programming) 5+ years "
                                       "hands on python development * Development of RESTful APIs using the Python "
                                       "language * Strong knowledge of the Linux operating system * Highly desired: "
                                       "experience with Cloud Computing * Ability to quickly pick up new technologies *"
                                       " Work independently without needing lot of input, self-driven. * Experience "
                                       "with contributing to open source code is a plus",
                    "job_id": 70,
                    "job_title": "Software developer",
                    "link": "https://uscareers-rackspace.icims.com/jobs/13472/software-developer/job?mode=job&iis=Job+"
                            "Board+-+Indeed.com&iisn=Indeed.com",
                    "location_id": 1
                },
                {
                    "company_id": 9,
                    "job_description": "Qualifications Responsibilities * Design and implement production grade "
                                       "software at cloud scale * Partner with QE/Test, Support, Operations and Product"
                                       " management to ensure high quality software releases per schedule * Evaluate "
                                       "technical aspects of other developer s designs and proposals * Provide "
                                       "estimates for development effort The ideal candidate will have the following "
                                       "characteristics: * 5+ years of experience in software product development "
                                       "(design, coding, system engineering, object oriented programming) 5+ years "
                                       "hands on python development * Development of RESTful APIs using the Python "
                                       "language * Strong knowledge of the Linux operating system * Highly desired: "
                                       "experience with Cloud Computing * Ability to quickly pick up new technologies "
                                       "* Work independently without needing lot of input, self-driven. * Experience "
                                       "with contributing to open source code is a plus",
                    "job_id": 71,
                    "job_title": "Senior Python Developer",
                    "link": "https://uscareers-rackspace.icims.com/jobs/11524/senior-python-developer/job?mode=job&iis="
                            "Job+Board+-+Indeed.com&iisn=Indeed.com",
                    "location_id": 1
                },
                {
                    "company_id": 9,
                    "job_description": "Responsibilities: Write thick client front-end code in Javascript, HTML, and "
                                       "CSS Build new features and fix bugs Write clean and maintainable code using "
                                       "engineering best practices (unit testing, source control, continuous "
                                       "integration, automation, design patterns, etc.) Work with other software "
                                       "engineers, product managers, user experience designers, and operations "
                                       "engineers on a daily basis Mentor and guide less experienced team members to "
                                       "provide technical direction Provide Fanatical support of all production "
                                       "software on which you currently work Qualifications The ideal candidate will "
                                       "have the following: BS in Computer Science or related field with 5+ years "
                                       "practical engineering experience in building large-scale web-based applications"
                                       " Experience building applications with an object oriented Javascript framework"
                                       " (Google Closure, Backbone, Spine, etc) Advanced knowledge of DOM manipulation"
                                       " (jQuery, Dojo, etc) Ability to turn mocks from designers into the right HTML "
                                       "and CSS/LESS/SASS Disciplined approach to testing and quality engineering "
                                       "(Jasmine, QUnit, YUITest, etc) Excellent verbal and written communication "
                                       "skills Top candidates may also have some of the following: Experience with a "
                                       "server-side framework like Django, Node.js, or Rails Experience with "
                                       "cross-browser compatibility and browser degradation strategies Good sense of "
                                       "what is required for a great user interface and experience Familiarity or "
                                       "experience with Service Oriented Architecture and RESTful web services "
                                       "Familiarity or experience with Agile engineering practices (test driven "
                                       "development, continuous integration and pair programming, etc.) Good "
                                       "understanding of web technologies (HTTP, Apache, MySQL, HTTP Proxies) and "
                                       "familiarity with UNIX/Linux",
                    "job_id": 72,
                    "job_title": "Senior Javascript Developer",
                    "link": "https://uscareers-rackspace.icims.com/jobs/11872/senior-javascript-developer/job?mode=job&"
                            "iis=Job+Board+-+Indeed.com&iisn=Indeed.com",
                    "location_id": 1
                },
                {
                    "company_id": 10,
                    "job_description": " Responsibilities: Interact with product managers to define and develop new "
                                       "products, features, and enhancements Build mockups and prototypes to "
                                       "communicate and refine product concepts Contribute scalable, production-ready "
                                       "code for user-facing features Develop reusable application components Promote "
                                       "best practices for web user experience Ideal candidate: Has a passion for "
                                       "consumer web applications and search engines Understands the end user and can "
                                       "create simple, elegant solutions Loves to learn and develop new skills "
                                       "continuously. Requirements: BS in Computer Science or related area, or relevant"
                                       " work experience Minimum of 2 years experience in web development as part of a"
                                       " cross-functional product team Hands-on expertise with HTML, CSS, and "
                                       "JavaScript Demonstrated experience with web user interface toolkits such as "
                                       "JQuery Familiarity with best practices for web usability and interaction design"
                                       " Deep understanding of browser capabilities, browser security concerns such as"
                                       " cross-site scripting, and cross-browser incompatibilities Experience "
                                       "developing server-side Java servlets, JSPs, and JSP tag libraries Experience "
                                       "with the full development life cycle of web applications from requirements to "
                                       "launch Experience building solutions for high traffic web sites a plus.",
                    "job_id": 73,
                    "job_title": "Front End Software Engineer - Search ",
                    "link": "http://www.indeed.com/viewjob?jk=8134cd20bc82db8b&q=company%3Aindeed+developer&tk=19gsvnbu"
                            "v19vi04t",
                    "location_id": 1
                },
                {
                    "company_id": 10,
                    "job_description": "As a Software Engineer, Client Implementation - Mobile Apply you will take the "
                                       "unfriendly mobile apply process and turn it into a pleasant experience for job "
                                       "seekers. Responsibilities: You want to work with a wide variety of technologies"
                                       " and constantly learn new things You take pride in designing creative, simple "
                                       "solutions to challenging problems You are detail-oriented and have an "
                                       "outstanding work ethic You enjoy documenting and sharing knowledge with the "
                                       "team You have a strong sense of ownership for everything you build and want to "
                                       "see your work make a difference every day Take ownership of each "
                                       "client-specific implementation that you work on Communicate and collaborate "
                                       "with cross-functional teams Manage multiple priorities successfully Follow and "
                                       "drive development best practices for design, performance and scalability "
                                       "Improve and update internal processes, tools, and documentation in order to "
                                       "keep up with growing demand Requirements: Have a Bachelor s Degree in a related"
                                       " field Have 1-3 years of experience and proficiency in object-oriented "
                                       "programming (Java/C++). Be fluent in Javascript, HTML, CSS and XML Familiarity "
                                       "with scripting languages such as Python/Ruby is big plus Be familiar with "
                                       "browser automation frameworks (Selenium/PhantomJS/CasperJS) Have strong coding,"
                                       " problem solving, and design skills, and have both a broad and deep knowledge "
                                       "of data structures and algorithms Be comfortable working in a UNIX/Linux "
                                       "environment Communicate clearly with both technical and non-technical users Be "
                                       "detail oriented with strong organiz ational skills Thrive in a fast paced "
                                       "environment",
                    "job_id": 75,
                    "job_title": "Software Engineer, Client Implementation - Mobile Apply ",
                    "link": "http://www.indeed.com/viewjob?jk=097acafd3b9251cc&q=company%3Aindeed+developer&tk=19gsvnbu"
                            "v19vi04t",
                    "location_id": 1
                },
                {
                    "company_id": 10,
                    "job_description": "Responsibilities: Interact with product managers to define and develop new "
                                       "products, features, and enhancements Build mockups and prototypes to "
                                       "communicate and refine product concepts Contribute scalable, production-ready "
                                       "code for user-facing features Develop reusable application components Promote "
                                       "best practices for web user experience We re looking for someone who: Has a "
                                       "passion for consumer web applications and search engines Understands the end "
                                       "user and can create simple, elegant solutions Loves to learn and develop new "
                                       "skills continuously Requirements: BS in Computer Science or related area, or "
                                       "relevant work experience Minimum of 3 years experience in web development as "
                                       "part of a cross-functional product team Hands-on expertise with HTML, CSS, and "
                                       "JavaScript Demonstrated experience with web user interface toolkits such as "
                                       "JQuery Familiarity with best practices for web usability and interaction design"
                                       " Deep understanding of browser capabilities, browser security concerns such as "
                                       "cross-site scripting, and cross-browser incompatibilities Experience developing"
                                       " server-side Java servlets, JSPs, and JSP tag libraries Experience with the "
                                       "full development life cycle of web applications from requirements to launch "
                                       "Experience building solutions for high traffic web sites a plus",
                    "job_id": 76,
                    "job_title": "Front End Software Engineer ",
                    "link": "http://www.indeed.com/viewjob?jk=7bbe53a5ad085229&q=company%3Aindeed+developer&tk=19gt0971"
                            "d19vi7fu",
                    "location_id": 3
                },
                {
                    "company_id": 10,
                    "job_description": "Requirements: Extensive experience with Java or a similar language Superb "
                                       "knowledge of algorithms and data structures. Excellent programming skills A "
                                       "track record of successful delivery of new applications and services A degree "
                                       "in Computer Science or equivalent experience Passion for solving hard problems "
                                       "that matter Nice to Have: A deep understanding of the many ways systems can "
                                       "fail Knowledge of how to build systems resilient to failure Good taste and an "
                                       "intuition for balanced, simple solutions Strong knowledge of operating system "
                                       "behaviors, especially regarding stability, performance, and correctness "
                                       "Expertise in building platforms used by other developers to build new products "
                                       "Experience with service-oriented architectures Academic or real-world "
                                       "experience building distributed systems, including distributed consensus "
                                       "protocols like Paxos or Raft. Experience with distributed data stores like "
                                       "Dynamo, Cassandra, HDFS, and ZooKeeper. The ability to clearly and cogently "
                                       "describe complex ideas The ability to write automated tests to ensure the "
                                       "correctness of complex systems A watch that measures time in milliseconds, "
                                       "microseconds, and nanoseconds",
                    "job_id": 77,
                    "job_title": "Senior Software Engineer - Scalable Systems ",
                    "link": "http://www.indeed.com/viewjob?jk=dd410c2fe0a82d75&q=company%3Aindeed+developer&tk=19gt0blm"
                            "p19vi389",
                    "location_id": 2
                },
                {
                    "company_id": 3,
                    "job_description": "Amazon Web Services (AWS) in Seattle is actively seeking a Senior Software "
                                       "Developer to help create a brand new service. This is an excellent opportunity "
                                       "to join a cutting edge team developing customer focused products. Relocation "
                                       "assistance is available. Join AWS to help mobile developers build great "
                                       "cloud-backed apps! As a member of the AWS Mobile team, you will develop "
                                       "services which cater to the needs of mobile developers who build apps for iOS, "
                                       "Android, Kindle, and the mobile web.We believe that cloud-backed mobile and "
                                       "device applications are a big deal, and our customers are developers who think "
                                       "likewise. We are driven to support our customers in their endeavors, providing "
                                       "software and services to help them use AWS as the foundation for their apps. "
                                       "This is a unique opportunity to influence the mobile app development community "
                                       "in a big way.This role will be responsible for building web service APIs that "
                                       "interact with mobile applications.",
                    "job_id": 78,
                    "job_title": "Software Developer - Amazon Web Services",
                    "link": "http://www.amazon.jobs/jobs/295855/software-developer-amazon-web-services-new-mobile-"
                            "service",
                    "location_id": 2
                },
                {
                    "company_id": 3,
                    "job_description": "We re looking for product-aware engineers who are thoughtful, responsible and "
                                       "passionate builders who appreciate user experience. We re looking for someone "
                                       "who is not only well versed in iOS development, but also has a strong "
                                       "understanding of good UX and isn t afraid to get their hands dirty in backend "
                                       "code. We believe that great product people use lots of products, so if you re "
                                       "an active user of Goodreads, we are listening. Come to join us to shape the "
                                       "future how people find their next favorite book.",
                    "job_id": 79,
                    "job_title": "Senior iOS Developer",
                    "link": "http://www.amazon.jobs/jobs/303634/senior-ios-developer",
                    "location_id": 3
                }
            ]
        }
        actual = requests.get("http://104.130.229.90:5000/api/job").json()
        self.assertEqual(expected, actual)

    def test_getting_job(self):
        expected = {
            "company_id": 2,
            "job_description": "Design, configure, and implement our data systems and stream processing pipelines/nCode"
                               " analytics jobs, web services, and other components/nWork with operations to build and"
                               " configure maintainable, resource-efficient systems/nWork with data pipelines using "
                               "Kafka, Cassandra, Spark/nLeverage Event processing technologies to deliver real time "
                               "analytics features/nDevelop a cloud service that would be processing billions of events"
                               " a day/nLeverage fast data pipelines for real time analytics on various Oracle SaaS "
                               "applications/nContribute ideas for continually improving the team s productivity, job "
                               "enjoyment, and code quality./nActively mentor junior developers to develop their "
                               "technical expertise/nHave fun engineering software and scalable systems",
            "job_id": 1,
            "job_title": "Software Developer 4",
            "link": "https://oracle.taleo.net/careersection/2/jobdetail.ftl?job=90953",
            "location_id": 3
        }
        actual = requests.get("http://104.130.229.90:5000/api/job/1").json()
        self.assertEqual(expected, actual)

    def test_getting_nonexistent_job(self):
        expected = {"error": "Item does not exist"}
        actual = requests.get("http://104.130.229.90:5000/api/job/1123456789").json()
        self.assertEqual(expected, actual)

    def test_getting_companies(self):
        expected = {
            "Companies": [
                {
                    "company_description": "Search engine",
                    "company_id": 1,
                    "company_image": "images/company_images/google_logo.png",
                    "company_name": "Google",
                    "company_site": "www.google.com"
                },
                {
                    "company_description": "Database",
                    "company_id": 2,
                    "company_image": "images/company_images/oracle_logo.jpg",
                    "company_name": "Oracle",
                    "company_site": "www.oracle.com"
                },
                {
                    "company_description": "Online shopping",
                    "company_id": 3,
                    "company_image": "images/company_images/amazon_logo.jpeg",
                    "company_name": "Amazon",
                    "company_site": "www.amazon.com"
                },
                {
                    "company_description": "Social Media",
                    "company_id": 4,
                    "company_image": "images/company_images/facebook_logo.png",
                    "company_name": "Facebook",
                    "company_site": "www.facebook.com"
                },
                {
                    "company_description": "Social Media",
                    "company_id": 5,
                    "company_image": "images/company_images/twitter_logo.png",
                    "company_name": "Twitter",
                    "company_site": "www.twitter.com"
                },
                {
                    "company_description": "Online resume",
                    "company_id": 6,
                    "company_image": "images/company_images/linkedin_logo.png",
                    "company_name": "LinkedIn",
                    "company_site": "www.linkedin.com"
                },
                {
                    "company_description": "computer",
                    "company_id": 7,
                    "company_image": "images/company_images/ibm_logo.jpg",
                    "company_name": "IBM",
                    "company_site": "www.ibm.com"
                },
                {
                    "company_description": "Cloud service",
                    "company_id": 8,
                    "company_image": "images/company_images/dropbox_logo.png",
                    "company_name": "Dropbox",
                    "company_site": "www.dropbox.com"
                },
                {
                    "company_description": "Cloud server provider",
                    "company_id": 9,
                    "company_image": "images/company_images/rackspace_logo.png",
                    "company_name": "Rackspace",
                    "company_site": "www.rackspace.com"
                },
                {
                    "company_description": "Online yellow page for jobs",
                    "company_id": 10,
                    "company_image": "images/company_images/indeed_logo.png",
                    "company_name": "Indeed",
                    "company_site": "www.indeed.com"
                }
            ]
        }
        actual = requests.get("http://104.130.229.90:5000/api/company").json()
        self.assertEqual(expected, actual)

    def test_getting_company(self):
        expected = {
            "company_description": "Search engine",
            "company_id": 1,
            "company_image": "images/company_images/google_logo.png",
            "company_name": "Google",
            "company_site": "www.google.com"
        }
        actual = requests.get('http://104.130.229.90:5000/api/company/1').json()
        self.assertEqual(expected, actual)

    def test_getting_nonexistent_company(self):
        expected = {"error": "Item does not exist"}
        actual = requests.get("http://104.130.229.90:5000/api/company/1123456789").json()
        self.assertEqual(expected, actual)

    def test_getting_languages(self):
        expected = {
            "languages": [
                {
                    "language_description": "Muti platiform Language",
                    "language_id": 1,
                    "language_image": "images/language_icon/java_icon.png",
                    "language_name": "Java",
                    "language_wiki_description": "Java is a general-purpose computer programming language that is "
                                                 "concurrent, class-based, object-oriented, and specifically designed "
                                                 "to have as few implementation dependencies as possible. It is "
                                                 "intended to let application developers  write once, run anywhere  "
                                                 "(WORA), meaning that compiled Java code can run on all platforms that"
                                                 " support Java without the need for recompilation. Java applications "
                                                 "are typically compiled to bytecode that can run on any Java virtual "
                                                 "machine (JVM) regardless of computer architecture. As of 2015, Java "
                                                 "is one of the most popular programming languages in use, "
                                                 "particularly for client-server web applications, with a reported 9 "
                                                 "million developers. Java was originally developed by James Gosling at"
                                                 " Sun Microsystems (which has since merged into Oracle Corporation) "
                                                 "and released in 1995 as a core component of Sun Microsystems  Java "
                                                 "platform. The language derives much of its syntax from C and C++, but"
                                                 " it has fewer low-level facilities than either of them.",
                    "language_wiki_link": "http://en.wikipedia.org/wiki/Java_%28programming_language%29"
                },
                {
                    "language_description": "great Language",
                    "language_id": 2,
                    "language_image": "images/language_icon/cpp_icon.png",
                    "language_name": "C++",
                    "language_wiki_description": "C++ is a general-purpose programming language. It has imperative, "
                                                 "object-oriented and generic programming features, while also "
                                                 "providing the facilities for low-level memory manipulation.",
                    "language_wiki_link": "http://en.wikipedia.org/wiki/C%2B%2B"
                },
                {
                    "language_description": "Web Language",
                    "language_id": 3,
                    "language_image": "images/language_icon/php_icon.png",
                    "language_name": "PHP",
                    "language_wiki_description": "PHP is a server-side scripting language designed for web development "
                                                 "but also used as a general-purpose programming language. As of "
                                                 "January 2013, PHP was installed on more than 240 million websites "
                                                 "(39% of those sampled) and 2.1 million web servers. Originally "
                                                 "created by Rasmus Lerdorf in 1994, the reference implementation of "
                                                 "PHP (powered by the Zend Engine) is now produced by The PHP Group. "
                                                 "While PHP originally stood for Personal Home Page, it now stands for "
                                                 "PHP: Hypertext Preprocessor, which is a recursive backronym.",
                    "language_wiki_link": "http://en.wikipedia.org/wiki/PHP"
                },
                {
                    "language_description": "simple Language",
                    "language_id": 4,
                    "language_image": "images/language_icon/python_icon.png",
                    "language_name": "Python",
                    "language_wiki_description": "Python is a widely used general-purpose, high-level programming "
                                                 "language. Its design philosophy emphasizes code readability, and its "
                                                 "syntax allows programmers to express concepts in fewer lines of code "
                                                 "than would be possible in languages such as C++ or Java. The language"
                                                 " provides constructs intended to enable clear programs on both a "
                                                 "small and large scale.",
                    "language_wiki_link": "http://en.wikipedia.org/wiki/Python_%28programming_language%29"
                },
                {
                    "language_description": "web Language",
                    "language_id": 5,
                    "language_image": "images/language_icon/javascript_icon.png",
                    "language_name": "Javascript",
                    "language_wiki_description": "JavaScript is a dynamic computer programming language. It is most "
                                                 "commonly used as part of web browsers, whose implementations allow "
                                                 "client-side scripts to interact with the user, control the browser, "
                                                 "communicate asynchronously, and alter the document content that is "
                                                 "displayed. It is also used in server-side network programming with "
                                                 "runtime environments such as Node.js, game development and the "
                                                 "creation of desktop and mobile applications. With the rise of the "
                                                 "single-page web app and JavaScript-heavy sites, it is increasingly "
                                                 "being used as a compile target for source-to-source compilers from "
                                                 "both dynamic languages and static languages.",
                    "language_wiki_link": "http://en.wikipedia.org/wiki/JavaScript"
                },
                {
                    "language_description": "Apple Language",
                    "language_id": 6,
                    "language_image": "images/language_icon/objective-c_icon.png",
                    "language_name": "Objective-C",
                    "language_wiki_description": "Objective-C is a general-purpose, object-oriented programming "
                                                 "language that adds Smalltalk-style messaging to the C programming "
                                                 "language. It is the main programming language used by Apple for the "
                                                 "OS X and iOS operating systems, and their respective application "
                                                 "programming interfaces (APIs), Cocoa and Cocoa Touch.",
                    "language_wiki_link": "http://en.wikipedia.org/wiki/Objective-C"
                },
                {
                    "language_description": "Microsoft Language",
                    "language_id": 7,
                    "language_image": "images/language_icon/csharp_icon.png",
                    "language_name": "CSharp",
                    "language_wiki_description": "C# is a multi-paradigm programming language encompassing strong "
                                                 "typing, imperative, declarative, functional, generic, object-oriented"
                                                 " (class-based), and component-oriented programming disciplines. It "
                                                 "was developed by Microsoft within its  NET initiative and later "
                                                 "approved as a standard by Ecma (ECMA-334) and ISO "
                                                 "(ISO/IEC 23270:2006). C# is one of the programming languages designed"
                                                 " for the Common Language Infrastructure.",
                    "language_wiki_link": "http://en.wikipedia.org/wiki/C_Sharp_(programming_language)"
                },
                {
                    "language_description": "Microsoft Language",
                    "language_id": 8,
                    "language_image": "images/language_icon/vbnet_icon.png",
                    "language_name": "Visual Basic.NET",
                    "language_wiki_description": "Visual Basic  NET (VB.NET) is a multi-paradigm, high level "
                                                 "programming language, implemented on the  NET Framework. Microsoft "
                                                 "launched VB.NET in 2002 as the successor to its original Visual Basic"
                                                 " language. Although the  NET portion was dropped in 2005, this "
                                                 "article uses Visual Basic  NET to refer to all Visual Basic languages"
                                                 " releases since 2002, in order to distinguish between them and the "
                                                 "classic Visual Basic. Along with Visual C#, it is one of the two main"
                                                 " languages targeting the  NET framework.",
                    "language_wiki_link": "http://en.wikipedia.org/wiki/Visual_Basic_.NET"
                },
                {
                    "language_description": "Microsoft Language",
                    "language_id": 9,
                    "language_image": "images/language_icon/vb_icon.png",
                    "language_name": "Visual Basic",
                    "language_wiki_description": "Visual Basic is a third-generation event-driven programming language "
                                                 "and integrated development environment (IDE) from Microsoft for its "
                                                 "COM programming model first released in 1991. Microsoft intended "
                                                 "Visual Basic to be relatively easy to learn and use. Visual Basic was"
                                                 " derived from BASIC and enables the rapid application development "
                                                 "(RAD) of graphical user interface (GUI) applications, access to "
                                                 "databases using Data Access Objects, Remote Data Objects, or ActiveX "
                                                 "Data Objects, and creation of ActiveX controls and objects.",
                    "language_wiki_link": "http://en.wikipedia.org/wiki/Visual_Basic"
                },
                {
                    "language_description": "great Language",
                    "language_id": 10,
                    "language_image": "images/language_icon/c_icon.png",
                    "language_name": "C",
                    "language_wiki_description": "C is a general-purpose, imperative computer programming language. It "
                                                 "supports structured programming, lexical variable scope and "
                                                 "recursion, while a static type system prevents many unintended "
                                                 "operations. By design, C provides constructs that map efficiently to "
                                                 "typical machine instructions, and therefore it has found lasting use "
                                                 "in applications that had formerly been coded in assembly language, "
                                                 "including operating systems, as well as various application software "
                                                 "for computers ranging from supercomputers to embedded systems.",
                    "language_wiki_link": "http://en.wikipedia.org/wiki/C_(programming_language)"
                }
            ]
        }
        actual = requests.get("http://104.130.229.90:5000/api/language").json()
        self.assertEqual(expected, actual)

    def test_getting_language(self):
        expected = {
            "language_description": "Muti platiform Language",
            "language_id": 1,
            "language_image": "images/language_icon/java_icon.png",
            "language_name": "Java",
            "language_wiki_description": "Java is a general-purpose computer programming language that is concurrent, "
                                         "class-based, object-oriented, and specifically designed to have as few "
                                         "implementation dependencies as possible. It is intended to let application "
                                         "developers  write once, run anywhere  (WORA), meaning that compiled Java code"
                                         " can run on all platforms that support Java without the need for "
                                         "recompilation. Java applications are typically compiled to bytecode that can "
                                         "run on any Java virtual machine (JVM) regardless of computer architecture. As"
                                         " of 2015, Java is one of the most popular programming languages in use, "
                                         "particularly for client-server web applications, with a reported 9 million "
                                         "developers. Java was originally developed by James Gosling at Sun "
                                         "Microsystems (which has since merged into Oracle Corporation) and released in"
                                         " 1995 as a core component of Sun Microsystems  Java platform. The language "
                                         "derives much of its syntax from C and C++, but it has fewer low-level "
                                         "facilities than either of them.",
            "language_wiki_link": "http://en.wikipedia.org/wiki/Java_%28programming_language%29"
        }
        actual = requests.get("http://104.130.229.90:5000/api/language/1").json()
        self.assertEqual(expected, actual)

    def test_getting_nonexistent_language(self):
        expected = {"error": "Item does not exist"}
        actual = requests.get("http://104.130.229.90:5000/api/language/1123456789").json()
        self.assertEqual(expected, actual)

    def test_getting_locations(self):
        expected = {
            "locations": [
                {
                    "location_description": "Austin is the capital of the US state of Texas and the seat of Travis "
                                            "County. Located in Central Texas, Austin is the 11th-most populous city in"
                                            " the United States and the fourth-most populous city in Texas.",
                    "location_id": 1,
                    "location_image": "static/images/location_icon/austin.jpg",
                    "location_name": "Austin, TX"
                },
                {
                    "location_description": "Seattle is a coastal seaport city and the seat of King County, in the U.S."
                                            " state of Washington. With an estimated 652,405 residents as of 2013, "
                                            "Seattle is the largest city in both the State of Washington ...",
                    "location_id": 2,
                    "location_image": "static/images/location_icon/seattle.jpg",
                    "location_name": "Seattle, WA"
                },
                {
                    "location_description": "San Francisco, officially the City and County of San Francisco, is the "
                                            "cultural, commercial and financial center of Northern California.",
                    "location_id": 3,
                    "location_image": "static/images/location_icon/san_francisco.jpg",
                    "location_name": "San Francisco, CA"
                },
                {
                    "location_description": "Los Angeles, officially the City of Los Angeles, often known by its "
                                            "initials L.A., is a major city in California s Southern California region,"
                                            " approximately 342 miles south of San Francisco.",
                    "location_id": 4,
                    "location_image": "static/images/location_icon/los_anglos.jpg",
                    "location_name": "Los Angles, CA"
                },
                {
                    "location_description": "New York - often called New York City or the City of New York to "
                                            "distinguish it from the State of New York, of which it is a part - is the "
                                            "most populous city in the United States and the center of the ...",
                    "location_id": 5,
                    "location_image": "static/images/location_icon/new_york_city.jpg",
                    "location_name": "New York City, NY"
                },
                {
                    "location_description": "Boston is the capital and largest city of the Commonwealth of "
                                            "Massachusetts in the United States. Boston also serves as county seat of "
                                            "Suffolk County.",
                    "location_id": 6,
                    "location_image": "static/images/location_icon/boston.jpg",
                    "location_name": "Boston, MA"
                },
                {
                    "location_description": "Dallas is a major city in Texas and is the largest urban center of the "
                                            "fourth most populous metropolitan area in the United States. The city "
                                            "proper ranks ninth in the U.S. and third in Texas after Houston and San "
                                            "Antonio.",
                    "location_id": 7,
                    "location_image": "static/images/location_icon/dallas.jpg",
                    "location_name": "Dallas, TX"
                },
                {
                    "location_description": "San Jose is the third-largest city in California, the tenth-largest in the"
                                            " United States, and the county seat of Santa Clara County. San Jose is the"
                                            " largest city within the San Francisco Bay Area and the largest city in "
                                            "Northern California.",
                    "location_id": 8,
                    "location_image": "static/images/location_icon/san_jose.jpg",
                    "location_name": "San Jose, CA"
                },
                {
                    "location_description": "Mountain View is a city in Santa Clara County, in the Bay Area of "
                                            "California.",
                    "location_id": 9,
                    "location_image": "static/images/location_icon/mountain_view.jpg",
                    "location_name": "Mountain View, CA"
                },
                {
                    "location_description": "Menlo Park is an affluent city at the eastern edge of San Mateo County, "
                                            "in the San Francisco Bay Area of California, in the United States.",
                    "location_id": 10,
                    "location_image": "static/images/location_icon/menlo_park.jpg",
                    "location_name": "Menlo Park, CA"
                }
            ]
        }
        actual = requests.get("http://104.130.229.90:5000/api/location").json()
        self.assertEqual(expected, actual)

    def test_getting_location(self):
        expected = {
            "location_description": "Austin is the capital of the US state of Texas and the seat of Travis County. "
                                    "Located in Central Texas, Austin is the 11th-most populous city in the United "
                                    "States and the fourth-most populous city in Texas.",
            "location_id": 1,
            "location_image": "static/images/location_icon/austin.jpg",
            "location_name": "Austin, TX"
        }
        actual = requests.get("http://104.130.229.90:5000/api/location/1").json()
        self.assertEqual(expected, actual)

    def test_getting_nonexistent_location(self):
        expected = {"error": "Item does not exist"}
        actual = requests.get("http://104.130.229.90:5000/api/location/1123456789").json()
        self.assertEqual(expected, actual)

    def test_getting_skillsets(self):
        expected = {
            "Skillsets": [
                {
                    "skillset_description": "Spring, J2EE, Hibernate",
                    "skillset_id": 1,
                    "skillset_image": "static/images/skillset_icon/web_app_backend_icon.png",
                    "skillset_name": "Web app, Back-end",
                    "skillset_wiki_description": "A web application or web app is any software that runs in a web "
                                                 "browser. It is created in a browser-supported programming language "
                                                 "(such as the combination of JavaScript, HTML and CSS) and relies on a"
                                                 " web browser to render the application.",
                    "skillset_wiki_link": "http://en.wikipedia.org/wiki/Front_and_back_ends"
                },
                {
                    "skillset_description": "Mobile computing, IOS, Andriod",
                    "skillset_id": 2,
                    "skillset_image": "static/images/skillset_icon/mobile_computing_icon.png",
                    "skillset_name": "Mobile computing",
                    "skillset_wiki_description": "Mobile computing is human computer interaction by which a computer is"
                                                 " expected to be transported during normal usage. Mobile computing "
                                                 "involves mobile communication, mobile hardware, and mobile software. "
                                                 "Communication issues include ad hoc and infrastructure networks as "
                                                 "well as communication properties, protocols, data formats and "
                                                 "concrete technologies. Hardware includes mobile devices or device "
                                                 "components. Mobile software deals with the characteristics and "
                                                 "requirements of mobile applications.",
                    "skillset_wiki_link": "http://en.wikipedia.org/wiki/Mobile_computing"
                },
                {
                    "skillset_description": "Network administration, Cloud computing",
                    "skillset_id": 3,
                    "skillset_image": "static/images/skillset_icon/network_icon.png",
                    "skillset_name": "Network",
                    "skillset_wiki_description": "A computer network or data network is a telecommunications network "
                                                 "which allows computers to exchange data. In computer networks, "
                                                 "networked computing devices pass data to each other along data "
                                                 "connections (network links). Data is transferred in the form of "
                                                 "packets. The connections between nodes are established using either "
                                                 "cable media or wireless media. The best-known computer network is the"
                                                 " Internet.",
                    "skillset_wiki_link": "http://en.wikipedia.org/wiki/Computer_network"
                },
                {
                    "skillset_description": "Html, javascript, CSS",
                    "skillset_id": 4,
                    "skillset_image": "static/images/skillset_icon/web_frontend_icon.png",
                    "skillset_name": "Web Front-end",
                    "skillset_wiki_description": "In software engineering, the terms front end and back end are "
                                                 "distinctions which refer to the separation of concerns between a "
                                                 "presentation layer and a data access layer respectively. The front "
                                                 "end is an interface between the user and the back end. The front and "
                                                 "back ends may be distributed amongst one or more systems.",
                    "skillset_wiki_link": "http://en.wikipedia.org/wiki/Front_and_back_ends"
                },
                {
                    "skillset_description": "Hadoop, big data",
                    "skillset_id": 5,
                    "skillset_image": "static/images/skillset_icon/bigdata_icon.png",
                    "skillset_name": "Big data",
                    "skillset_wiki_description": "Big data is a broad term for data sets so large or complex that "
                                                 "traditional data processing applications are inadequate. Challenges "
                                                 "include analysis, capture, curation, search, sharing, storage, "
                                                 "transfer, visualization, and information privacy.",
                    "skillset_wiki_link": "http://en.wikipedia.org/wiki/Big_data"
                },
                {
                    "skillset_description": "MySQL, NoSQL, MongoDB",
                    "skillset_id": 6,
                    "skillset_image": "static/images/skillset_icon/database_icon.png",
                    "skillset_name": "Database",
                    "skillset_wiki_description": "A database is an organized collection of data. The data is typically "
                                                 "organized to model aspects of reality in a way that supports "
                                                 "processes requiring information. For example, modelling the "
                                                 "availability of rooms in hotels in a way that supports finding a "
                                                 "hotel with vacancies.",
                    "skillset_wiki_link": "http://en.wikipedia.org/wiki/Database"
                }
            ]
        }
        actual = requests.get("http://104.130.229.90:5000/api/skillset").json()
        self.assertEqual(expected, actual)

    def test_getting_skillset(self):
        expected = {
            "skillset_description": "Spring, J2EE, Hibernate",
            "skillset_id": 1,
            "skillset_image": "static/images/skillset_icon/web_app_backend_icon.png",
            "skillset_name": "Web app, Back-end",
            "skillset_wiki_description": "A web application or web app is any software that runs in a web browser. It "
                                         "is created in a browser-supported programming language (such as the "
                                         "combination of JavaScript, HTML and CSS) and relies on a web browser to "
                                         "render the application.",
            "skillset_wiki_link": "http://en.wikipedia.org/wiki/Front_and_back_ends"
        }
        actual = requests.get("http://104.130.229.90:5000/api/skillset/1").json()
        self.assertEqual(expected, actual)

    def test_getting_nonexistent_skillset(self):
        expected = {"error": "Item does not exist"}
        actual = requests.get("http://104.130.229.90:5000/api/skillset/1123456789").json()
        self.assertEqual(expected, actual)

    def test_getting_members(self):
        expected = {
            "Members": [
                {
                    "member_bio": "BS in Computer Science. \\nExpected to graduate Dec 2015. \\nLanguage: Java, C++, "
                                  "PHP, SQL, Python.",
                    "member_commit": 78,
                    "member_id": 1,
                    "member_image": "static/images/member/Da_Meng.jpg",
                    "member_issue": 9,
                    "member_leader": 1,
                    "member_major_responsibility": "First team leader, assigning work to each team member, \\nhelping "
                                                   "communication within the team, collecting data, designing pages.",
                    "member_name": "Da Meng",
                    "member_unittest": 0
                },
                {
                    "member_bio": "Computer Science major, Korean minor.\\nGraduating on May 2015. \\nFluent in Java, "
                                  "C, Python, SQL.",
                    "member_commit": 15,
                    "member_id": 2,
                    "member_image": "static/images/member/Jin_Ho_Kim.jpg",
                    "member_issue": 5,
                    "member_leader": 0,
                    "member_major_responsibility": "Apiary Contribution, data entry, etc.",
                    "member_name": "Jin Ho Kim",
                    "member_unittest": 24
                },
                {
                    "member_bio": "Second team leader.\\nThird year University of Texas student pursuing \\nBachelor of"
                                  " Science degrees in Computer Science and Pure Mathematics. \\nExpected to graduate "
                                  "in August 2015. \\nFavorite Language is Python.",
                    "member_commit": 50,
                    "member_id": 3,
                    "member_image": "static/images/member/Kevin_Valle.jpg",
                    "member_issue": 25,
                    "member_leader": 2,
                    "member_major_responsibility": "First team leader, assigning work to each team member, \\nhelping "
                                                   "communication within the team, collecting data, designing pages.",
                    "member_name": "Kevin Valle",
                    "member_unittest": 15
                },
                {
                    "member_bio": "BSA in Computer Science with a Business Foundations Certificate. \\nExpected to "
                                  "graduate May 2015. \\nLanguage: Java, C, C#, Python, SQL",
                    "member_commit": 77,
                    "member_id": 4,
                    "member_image": "static/images/member/Chan_Hee_Park.jpg",
                    "member_issue": 11,
                    "member_leader": 0,
                    "member_major_responsibility": "Front-end development (HTML, CSS, JavaScript) \\nwith usage of "
                                                   "Twitter Bootstrap",
                    "member_name": "Chan Hee Park",
                    "member_unittest": 0
                },
                {
                    "member_bio": "Computer Science Major with CS Game Development Certificate. \\nExpected to graduate"
                                  " Dec. 2015. \\nSkill: C++, OpenGL, Java, Python.",
                    "member_commit": 115,
                    "member_id": 5,
                    "member_image": "static/images/member/Seung_Youp_Baek.png",
                    "member_issue": 19,
                    "member_leader": 0,
                    "member_major_responsibility": "Front end development.\\nStatic/dynamic page with HTML, CSS, "
                                                   "Bootstrap, and Javascript.\\nApiary, etc.",
                    "member_name": "Seung Youp Baek",
                    "member_unittest": 0
                }
            ]
        }
        actual = requests.get('http://104.130.229.90:5000/api/member').json()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()