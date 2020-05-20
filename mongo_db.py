import pymongo

#TODO: "mongodb+srv://AlexJonesCU:<Password>@cluster0-wstj3.gcp.mongodb.net/cpsc408-mongo-test?retryWrites=true&ssl_cert_reqs=CERT_NONE"


client = pymongo.MongoClient("mongodb+srv://AlexJonesCU:<Password>@cluster0-wstj3.gcp.mongodb.net/test?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
print(client.list_database_names())

db = client['cpsc-408-mongo-test']


#select document
#print all entries in the 'Student' database
for s in db.Student.find():
    print(s)

print("--------------------------------------------------------------------")

#print all student First Names with a major in Dance
for s in db.Student.find({"major":"DANCE"}):
    print(s['FirstName'])

print("--------------------------------------------------------------------")

#print all student First names and courses they are taking that are majoring in comp sci
for s in db.Student.find({"major":"CPSC"}):
    print(s['FirstName'], s['courses'])

print("--------------------------------------------------------------------")

#sort students in order of Student Id number(lowest to highest)
for s in db.Student.find().sort("StudentId", 1):
    print(s['StudentId'], s['FirstName'], s['LastName'])

print("--------------------------------------------------------------------")

#print all students named Antonio that are majoring in Bio
for s in db.Student.find({"major":"BIO","FirstName":"Antonio"}):
    print(s)

