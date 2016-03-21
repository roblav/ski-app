from lxml import html
import requests

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

data = {
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

print data


