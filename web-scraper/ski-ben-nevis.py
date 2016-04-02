from lxml import html
import requests
import pymongo
import datetime

page = requests.get('https://www.visitscotland.com/see-do/active/skiing-snowsports/conditions/nevis-range/')
tree = html.fromstring(page.content)

#Mountain Status

snowConditions = tree.xpath("//*[@id='wrapper']/section[3]/div/div[2]/div[1]/article[1]/p[1]/text()")

#print snowConditions

#This will create a list of runs and runsStatus:
lifts = tree.xpath('//*[@id="ski-lift-status"]/li/text()')
liftStatus = tree.xpath('//*[@id="ski-lift-status"]/li/span/text()')

#print lifts
#print liftStatus

#This will create a list of runs and runsStatus:
runs = tree.xpath("//*[@id='run-status']/li/text()")
runStatus = tree.xpath("//*[@id='run-status']/li/span[2]/text()")

#print runs
#print runStatus

# Create a list of the runType to add to data
skiRunGrades = [
    'blue','blue','blue','red','red','red',
    'red','red','blue','red','black','black',
    'red','black','black','blue','blue','black',
    'blue','blue','blue','blue','blue',
    'green','green','green','green','green','',
    '','',''
    ]

# Create list of MountainLifts
# Create list of MountainStatus
# Add record to MongoDB

# iterate over runs and status
# create a json structure to add to mongodb

#    "mountainStatus": [
#      {"runName":"Half Pipe", "runStatus": "closed", "runGrade":"blue"},
#      {"runName":"Ptarmigan Bowl", "runStatus": "open", "runGrade":"blue"}
#    ]

#today = datetime.date.today()
now = datetime.datetime.now()

data = {
    "datestamp": {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute
    },
    "resort": "nevis-range",
    "mountainStatus": [],
    "mountainRuns": [],
    "mountainLifts": []
}

data["mountainStatus"].append({"snowConditions": snowConditions})

for a, b in zip(lifts, liftStatus):
    data["mountainLifts"].append({"liftName": a, "liftStatus": b})

for a, b in zip(runs, runStatus):
    data["mountainRuns"].append({"runName": a, "runStatus": b})

for i, elem in enumerate(skiRunGrades):
    print(i, elem)
    data["mountainRuns"][i]["runGrade"] = elem

#print data

# Local Connection to Mongo DB
#try:
#    conn=pymongo.MongoClient()
#    print "Connected successfully!!!"
#except pymongo.errors.ConnectionFailure, e:
#   print "Could not connect to MongoDB: %s" % e
#conn
#
#db = conn.mydb
#db
#
#collection = db.my_collection
#collection

#collection.insert(data)

#Heroku Connection

# If you are using a PaaS add-on integration e.g. via Heroku, the URI is usually available via an environment variable, often
# named "MONGOLAB_URI". Consult the documentation for the add-on you are using.
mongolab_uri = "mongodb://heroku_s1bc2vtt:vkv4ltahhpr1r417v95rqcbi4r@ds025469.mlab.com:25469/heroku_s1bc2vtt"

#https://github.com/mongolab/mongodb-driver-examples/blob/master/python/pymongo_production_connection_example.py

try:
    conn = pymongo.MongoClient(mongolab_uri)
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e

conn

db = conn.get_default_database()

collection = db.my_collection

collection.insert(data)