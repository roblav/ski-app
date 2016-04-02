from lxml import html
import requests
import pymongo
import datetime

page = requests.get('http://www.cairngormmountain.org/lifts-pistes/')
tree = html.fromstring(page.content)

#Mountain Status

operationUpdate = tree.xpath("//h4[contains(text(),'Operations Update:')]/following-sibling::text()[1]")
snowLevel = tree.xpath("//h4[contains(text(),'Snow Level:')]/following-sibling::text()[1]")
verticalRuns = tree.xpath("//h4[contains(text(),'Vertical Runs:')]/following-sibling::text()[1]")

#This will create a list of runs and runsStatus:
lifts = tree.xpath("//h4[contains(text(),'Mountain lifts')]/parent::li/following-sibling::li/h4//text()")
liftStatus = tree.xpath("//h4[contains(text(),'Mountain lifts')]/parent::li/following-sibling::li/p/a/text()")

#print lifts
#print liftStatus

#This will create a list of runs and runsStatus:
runs = tree.xpath("//h4[contains(text(),'Mountain Run')]/parent::li/following-sibling::li/h4//text()")
runStatus = tree.xpath("//h4[contains(text(),'Mountain Run')]/parent::li/following-sibling::li/p/a/text()")

# Create a list of the runType to add to data
skiRunGrades = [
    'red','green','green','green','green','green',
    'green','green','blue','green','blue','red',
    'blue','red','blue','red','blue','blue',
    'green','green','green','green','blue',
    'blue','red','black','red','red','red',
    'black','blue','blue'
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
    "resort": "Cairngorm",
    "mountainStatus": [],
    "mountainRuns": [],
    "mountainLifts": []
}

data["mountainStatus"].append({"operationUpdate": operationUpdate})
data["mountainStatus"].append({"snowLevel": snowLevel})
data["mountainStatus"].append({"verticalRuns": verticalRuns})

for a, b in zip(lifts, liftStatus):
    data["mountainLifts"].append({"liftName": a, "liftStatus": b})

for a, b in zip(runs, runStatus):
    data["mountainRuns"].append({"runName": a, "runStatus": b})

for i, elem in enumerate(skiRunGrades):
    #print(i, elem)
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